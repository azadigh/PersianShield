import urllib.request
import os
import json
import re
from datetime import datetime, timezone

REPO = os.getenv('GITHUB_REPOSITORY', 'azadigh/PersianShield')
HOMEPAGE = f"https://github.com/{REPO}"
LOCAL_EXTRA_FILE = "extra.txt"

CATEGORY_LABELS = {
    "persian":         "🇮🇷 Persian / Iranian",
    "ads":             "🚫 Ads Blocking",
    "privacy":         "🕵️ Privacy & Tracking",
    "annoyances":      "🙅 Annoyances",
    "cookie_consent":  "🍪 Cookie Consent",
    "anti_adblock":    "🛑 Anti-Adblock Killer",
    "security_light":  "🛡️ Security (Light)",
    "security_rules":  "🛡️ Security Rules",
    "crypto":          "⛏️ Crypto-mining",
    "security_heavy":  "🛡️ Security (Heavy)",
    "adult":           "🔞 Adult / NSFW",
}

SOURCES = {
    "persian": [
        ("PersianBlocker", "https://raw.githubusercontent.com/MasterKia/PersianBlocker/main/PersianBlocker.txt"),
        ("uBOPa", "https://raw.githubusercontent.com/nimasaj/uBOPa/master/uBOPa.txt"),
        ("AdBlock Iran", "https://raw.githubusercontent.com/farrokhi/adblock-iran/master/filter.txt"),
        ("AdBlockFA", "https://raw.githubusercontent.com/SlashArash/adblockfa/master/adblockfa.txt"),
        ("Persian Community List", "https://ideone.com/plain/K452p"),
    ],
    "ads": [
        ("EasyList", "https://easylist-downloads.adblockplus.org/easylist.txt"),
        ("Peter Lowe's Ad/Tracking", "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=0&mimetype=plaintext"),
        ("AdGuard Base", "https://filters.adtidy.org/extension/ublock/filters/2_optimized.txt"),
        ("AdGuard Mobile Ads", "https://filters.adtidy.org/extension/ublock/filters/11_optimized.txt"),
        ("uBlock filters", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt"),
        ("uBlock Unbreak", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt"),
        ("uBlock Quick fixes", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt"),
    ],
    "privacy": [
        ("EasyPrivacy", "https://easylist-downloads.adblockplus.org/easyprivacy.txt"),
        ("AdGuard Tracking Protection", "https://filters.adtidy.org/extension/ublock/filters/3_optimized.txt"),
        ("uBlock Privacy", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt"),
    ],
    "annoyances": [
        ("EasyList Cookie", "https://easylist-downloads.adblockplus.org/easylist-cookie.txt"),
        ("Fanboy's Annoyance", "https://easylist-downloads.adblockplus.org/fanboy-annoyance.txt"),
        ("Fanboy's Social", "https://easylist-downloads.adblockplus.org/fanboy-social.txt"),
        ("Fanboy's Notifications", "https://easylist-downloads.adblockplus.org/fanboy-notifications.txt"),
        ("AdGuard Annoyances", "https://filters.adtidy.org/extension/ublock/filters/14_optimized.txt"),
        ("AdGuard Social Media", "https://filters.adtidy.org/extension/ublock/filters/4_optimized.txt"),
        ("uBlock Annoyances", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt"),
    ],
    "cookie_consent": [
        ("AdGuard Cookie Notices", "https://filters.adtidy.org/extension/ublock/filters/18_optimized.txt"),
    ],
    "anti_adblock": [
        ("Anti-Adblock Killer", "https://raw.githubusercontent.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt"),
    ],
    "security_light": [
        ("oisd small", "https://small.oisd.nl/"),
    ],
    "security_rules": [
        ("uBlock Badware risks", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt"),
    ],
    "crypto": [
        ("NoCoin", "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt"),
    ],
    "security_heavy": [
        ("oisd full", "https://dbl.oisd.nl/"),
        ("StevenBlack unified hosts", "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"),
        ("Spam404", "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt"),
        ("Dandelion Sprout Anti-Malware", "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout%27s%20Anti-Malware%20List.txt"),
        ("CoinBlockerLists", "https://raw.githubusercontent.com/ZeroDot1/CoinBlockerLists/master/list_browser.txt"),
    ],
    "adult": [
        ("oisd NSFW", "https://nsfw.oisd.nl/"),
        ("Chad Mayfield Porn Top1M", "https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list"),
        ("StevenBlack porn", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts"),
    ],
}

FILES = {
    "persianshield-light.txt": {
        "title": "PersianShield Light ⭐ (Recommended)",
        "desc": "Lightweight & fast. Essential ads + privacy + annoyances + cookie + Persian + light security. NO adult content. Best balance for most users.",
        "categories": ["persian", "ads", "privacy", "annoyances", "cookie_consent", "security_light", "security_rules", "crypto"],
        "include_extra": True,
    },
    "persianshield-persian.txt": {
        "title": "PersianShield — Persian Only",
        "desc": "Only Persian/Iranian filters. NO adult content. Combine with other category lists.",
        "categories": ["persian"],
        "include_extra": True,
    },
    "persianshield-ads.txt": {
        "title": "PersianShield — Ads Blocking",
        "desc": "Global + Persian ad blocking only. NO adult content.",
        "categories": ["persian", "ads"],
        "include_extra": False,
    },
    "persianshield-privacy.txt": {
        "title": "PersianShield — Privacy & Tracking",
        "desc": "Blocks trackers and privacy invasion only. NO adult content.",
        "categories": ["privacy"],
        "include_extra": False,
    },
    "persianshield-annoyances.txt": {
        "title": "PersianShield — Annoyances + Cookie",
        "desc": "Removes cookie popups, social widgets, notifications. NO adult content.",
        "categories": ["annoyances", "cookie_consent"],
        "include_extra": False,
    },
    "persianshield-security.txt": {
        "title": "PersianShield — Security",
        "desc": "Blocks malware, phishing, cryptomining using a light domain list. NO adult content.",
        "categories": ["security_light", "security_rules", "crypto"],
        "include_extra": False,
    },
    "persianshield-ultimate.txt": {
        "title": "PersianShield Ultimate (Complete + Adult)",
        "desc": "MAXIMUM protection: everything INCLUDING anti-adblock killer and adult blocking. HEAVY. The only list with built-in adult blocking.",
        "categories": ["persian", "ads", "privacy", "annoyances", "cookie_consent", "anti_adblock", "security_heavy", "security_rules", "crypto", "adult"],
        "include_extra": True,
    },
    "pornlist.txt": {
        "title": "PornList — Standalone Adult Blocking",
        "desc": "Standalone adult/pornography blocking list. Add ON TOP of any other list (e.g., Light) to block adult content without the heavy Ultimate list.",
        "categories": ["adult"],
        "include_extra": False,
    },
}

LOCALHOST_NAMES = {"localhost", "localhost.localdomain", "broadcasthost", "local", "ip6-localhost"}
SOURCE_HEALTH = {}
GLOBAL_STATS = {"fetched_unique": 0, "merged_unique": 0}


def looks_like_ip(token):
    parts = token.split(".")
    return len(parts) == 4 and all(p.isdigit() for p in parts)


def is_valid_domain(d):
    if not d or "." not in d or looks_like_ip(d):
        return False
    return bool(re.match(r"^[a-z0-9.-]+\.[a-z]{2,}$", d))


def parse_line(line):
    line = line.strip()
    if not line:
        return None
    if line.startswith("!") or line.startswith("["):
        return None
    if line.startswith("#") and not line.startswith("##") and not line.startswith("#@"):
        return None
    parts = line.split()
    if len(parts) == 2 and parts[0] in ("0.0.0.0", "127.0.0.1", "::1"):
        d = parts[1].lower()
        return None if d in LOCALHOST_NAMES else f"||{d}^"
    if len(parts) == 1:
        token = parts[0]
        is_bare = (
            "##" not in token and "#" not in token and "$" not in token
            and "/" not in token and "|" not in token and "@" not in token
            and "*" not in token and "~" not in token and "^" not in token
            and "." in token and "://" not in token and not looks_like_ip(token)
        )
        if is_bare:
            d = token.lower().rstrip(".")
            return f"||{d}^" if len(d) > 3 else None
        return token
    return line


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (PersianShield)"})
        with urllib.request.urlopen(req, timeout=40) as r:
            text = r.read().decode("utf-8", errors="ignore")
        rules = {p for ln in text.splitlines() if (p := parse_line(ln))}
        SOURCE_HEALTH[url] = {"status": "ok", "rules": len(rules), "error": None}
        return rules
    except Exception as e:
        SOURCE_HEALTH[url] = {"status": "failed", "rules": 0, "error": str(e)}
        print(f"   ⚠️  FAILED ({e})")
        return set()


def read_local_extra(path=LOCAL_EXTRA_FILE):
    if not os.path.exists(path):
        print(f"   ⚠️  '{path}' not found — skipping custom rules.")
        return set()
    with open(path, "r", encoding="utf-8") as f:
        rules = {p for ln in f.read().splitlines() if (p := parse_line(ln))}
    print(f"   ✅ Loaded {len(rules):,} custom rules from {path}")
    return rules


def human_size(n):
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"


def build_header(cfg, rule_count, size_bytes):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    ver = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    lines = ["[Adblock Plus 2.0]", f"! Title: {cfg['title']}"]
    for dl in cfg["desc"].split(". "):
        lines.append(f"! {dl.strip()}.")
    lines += [
        f"! Homepage: {HOMEPAGE}",
        "! Coded by: github.com/azadigh and t.me/azadi_tg",
        f"! Version: {ver}", f"! Last modified: {now}",
        "! Expires: 1 days (update frequency)",
        f"! Total rules: {rule_count:,}", f"! File size: {human_size(size_bytes)}",
        "! License: MIT", "!",
        "! ==================== SOURCES / CREDITS ====================",
    ]
    seen = set()
    for cat in cfg["categories"]:
        label = CATEGORY_LABELS.get(cat, cat)
        if label in seen:
            continue
        seen.add(label)
        lines.append(f"! [{label}]")
        for name, url in SOURCES[cat]:
            status = SOURCE_HEALTH.get(url, {}).get("status", "?")
            mark = "✅" if status == "ok" else "❌"
            lines.append(f"!   {mark} {name}: {url}")
    lines.append("! ============================================================\n")
    return "\n".join(lines) + "\n"


def fetch_all_sources():
    cache = {}
    for cat, sources in SOURCES.items():
        cache[cat] = set()
        print(f"\n📂 Category: {CATEGORY_LABELS.get(cat, cat)}")
        for _, url in sources:
            print(f"   ⬇️  {url}")
            cache[cat] |= fetch(url)
        GLOBAL_STATS["fetched_unique"] += len(cache[cat])
        print(f"   → {len(cache[cat]):,} rules cached")
    return cache


def extract_domains(rules):
    domains = set()
    for rule in rules:
        if rule.startswith("@@"):
            continue
        if rule.startswith("||"):
            d = rule[2:].split("^")[0].split("/")[0].split("$")[0].strip().lower()
            if is_valid_domain(d):
                domains.add(d)
    return domains


def write_dns_formats(domains):
    sd = sorted(domains)
    with open("persianshield-dns-domains.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sd) + "\n")
    with open("persianshield-dns-hosts.txt", "w", encoding="utf-8") as f:
        f.write("# PersianShield hosts file\n")
        f.writelines(f"0.0.0.0 {d}\n" for d in sd)
    with open("persianshield-dns-dnsmasq.conf", "w", encoding="utf-8") as f:
        f.write("# PersianShield dnsmasq\n")
        f.writelines(f"address=/{d}/0.0.0.0\n" for d in sd)
    print(f"  ✅ DNS formats written — {len(sd):,} domains")


def write_stats(total_unique):
    ok = sum(1 for v in SOURCE_HEALTH.values() if v["status"] == "ok")
    data = {
        "schemaVersion": 1,
        "label": "Total Rules",
        "message": f"{total_unique:,}",
        "color": "brightgreen",
    }
    with open("stats.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\n📈 Stats: {total_unique:,} unique rules | {ok}/{len(SOURCE_HEALTH)} sources healthy")


def main():
    print("🚀 PersianShield — building tiered filter lists...\n")
    cache = fetch_all_sources()
    extra = read_local_extra()

    print("\n" + "=" * 60)
    print("📦 Generating output files...")
    print("=" * 60)

    summary = []
    ultimate_rules = set()
    for filename, cfg in FILES.items():
        rules = set()
        for cat in cfg["categories"]:
            rules |= cache.get(cat, set())
        if cfg.get("include_extra", False):
            rules |= extra
        if filename == "persianshield-ultimate.txt":
            ultimate_rules = set(rules)
        body = "\n".join(sorted(rules)) + "\n"
        size = len(body.encode("utf-8"))
        with open(filename, "w", encoding="utf-8") as f:
            f.write(build_header(cfg, len(rules), size))
            f.write(body)
        summary.append((filename, len(rules), size))
        print(f"  ✅ {filename} — {len(rules):,} rules — {human_size(size)}")

    # DNS formats from ultimate (comprehensive, includes adult)
    print("\n🌐 Generating DNS blocker formats (Pi-hole / AdGuard Home / dnsmasq)...")
    write_dns_formats(extract_domains(ultimate_rules))

    # Dedup stats
    GLOBAL_STATS["merged_unique"] = len(ultimate_rules)
    dedup_removed = GLOBAL_STATS["fetched_unique"] - len(
        set().union(*cache.values())
    )
    write_stats(len(set().union(*cache.values())))

    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"{'File':<32} {'Rules':>12} {'Size':>10}")
    print("-" * 60)
    for filename, count, size in summary:
        print(f"{filename:<32} {count:>12,} {human_size(size):>10}")
    print("-" * 60)
    print(f"🔁 Duplicate rules removed across sources: {dedup_removed:,}")
    ok = sum(1 for v in SOURCE_HEALTH.values() if v["status"] == "ok")
    print(f"🩺 Source health: {ok}/{len(SOURCE_HEALTH)} OK")
    if ok < len(SOURCE_HEALTH):
        print("\n⚠️  Failed sources:")
        for url, info in SOURCE_HEALTH.items():
            if info["status"] != "ok":
                print(f"   ❌ {url} → {info['error']}")
    print("\n🎉 All lists generated successfully!")


if __name__ == "__main__":
    main()
