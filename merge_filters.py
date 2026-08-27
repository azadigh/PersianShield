import urllib.request
import os
from datetime import datetime, timezone

REPO = os.getenv('GITHUB_REPOSITORY', 'azadigh/PersianShield')
HOMEPAGE = f"https://github.com/{REPO}"
LOCAL_EXTRA_FILE = "extra.txt"

# ============================================================
# CATEGORY LABELS (for header citation)
# ============================================================
CATEGORY_LABELS = {
    "persian":         "🇮🇷 Persian / Iranian",
    "ads":             "🚫 Ads Blocking",
    "privacy":         "🕵️ Privacy & Tracking",
    "annoyances":      "🙅 Annoyances",
    "security_light":  "🛡️ Security (Light)",
    "security_rules":  "🛡️ Security Rules",
    "crypto":          "⛏️ Crypto-mining",
    "security_heavy":  "🛡️ Security (Heavy)",
    "adult":           "🔞 Adult / NSFW",
}

# ============================================================
# SOURCES — split into granular categories to control size
# ============================================================
SOURCES = {
    # --- Persian (small) ---
    "persian": [
        ("PersianBlocker", "https://raw.githubusercontent.com/MasterKia/PersianBlocker/main/PersianBlocker.txt"),
        ("uBOPa", "https://raw.githubusercontent.com/nimasaj/uBOPa/master/uBOPa.txt"),
        ("AdBlock Iran", "https://raw.githubusercontent.com/farrokhi/adblock-iran/master/filter.txt"),
        ("AdBlockFA", "https://raw.githubusercontent.com/SlashArash/adblockfa/master/adblockfa.txt"),
        ("Persian Community List", "https://ideone.com/plain/K452p"),
    ],
    # --- Ads: adblock rules (medium) ---
    "ads": [
        ("EasyList", "https://easylist-downloads.adblockplus.org/easylist.txt"),
        ("Peter Lowe's Ad/Tracking", "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=0&mimetype=plaintext"),
        ("AdGuard Base", "https://filters.adtidy.org/extension/ublock/filters/2_optimized.txt"),
        ("AdGuard Mobile Ads", "https://filters.adtidy.org/extension/ublock/filters/11_optimized.txt"),
        ("uBlock filters", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt"),
        ("uBlock Unbreak", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt"),
        ("uBlock Quick fixes", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt"),
    ],
    # --- Privacy: adblock rules (medium) ---
    "privacy": [
        ("EasyPrivacy", "https://easylist-downloads.adblockplus.org/easyprivacy.txt"),
        ("AdGuard Tracking Protection", "https://filters.adtidy.org/extension/ublock/filters/3_optimized.txt"),
        ("uBlock Privacy", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt"),
    ],
    # --- Annoyances: adblock rules (medium) ---
    "annoyances": [
        ("EasyList Cookie", "https://easylist-downloads.adblockplus.org/easylist-cookie.txt"),
        ("Fanboy's Annoyance", "https://easylist-downloads.adblockplus.org/fanboy-annoyance.txt"),
        ("Fanboy's Social", "https://easylist-downloads.adblockplus.org/fanboy-social.txt"),
        ("Fanboy's Notifications", "https://easylist-downloads.adblockplus.org/fanboy-notifications.txt"),
        ("AdGuard Annoyances", "https://filters.adtidy.org/extension/ublock/filters/14_optimized.txt"),
        ("AdGuard Social Media", "https://filters.adtidy.org/extension/ublock/filters/4_optimized.txt"),
        ("uBlock Annoyances", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt"),
    ],
    # --- Security LIGHT domain list (small) ---
    "security_light": [
        ("oisd small", "https://small.oisd.nl/"),
    ],
    # --- Security adblock rules (small) ---
    "security_rules": [
        ("uBlock Badware risks", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt"),
    ],
    # --- Crypto-mining (small) ---
    "crypto": [
        ("NoCoin", "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt"),
    ],
    # --- Security HEAVY domain lists (very large) ---
    "security_heavy": [
        ("oisd full", "https://dbl.oisd.nl/"),
        ("StevenBlack unified hosts", "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"),
        ("Spam404", "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt"),
        ("Dandelion Sprout Anti-Malware", "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout%27s%20Anti-Malware%20List.txt"),
        ("CoinBlockerLists", "https://raw.githubusercontent.com/ZeroDot1/CoinBlockerLists/master/list_browser.txt"),
    ],
    # --- Adult (very large) ---
    "adult": [
        ("oisd NSFW", "https://nsfw.oisd.nl/"),
        ("Chad Mayfield Porn Top1M", "https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list"),
        ("StevenBlack porn", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts"),
    ],
}

# ============================================================
# OUTPUT FILES — porn kept OUT of category lists (to reduce size).
# Porn lives ONLY in: Ultimate (built-in) + standalone pornlist.txt
# ============================================================
FILES = {
    # ⭐ LIGHT — recommended (NO porn)
    "persianshield-light.txt": {
        "title": "PersianShield Light ⭐ (Recommended)",
        "desc": "Lightweight & fast. Essential ads + privacy + annoyances + Persian + light security. NO adult content. Best balance of protection and performance for most users.",
        "categories": ["persian", "ads", "privacy", "annoyances", "security_light", "security_rules", "crypto"],
        "include_extra": True,
    },
    # --- CATEGORY lists (NO porn, kept small) ---
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
        "title": "PersianShield — Annoyances",
        "desc": "Removes cookie popups, social widgets, and notification prompts. NO adult content.",
        "categories": ["annoyances"],
        "include_extra": False,
    },
    "persianshield-security.txt": {
        "title": "PersianShield — Security",
        "desc": "Blocks malware, phishing, and cryptomining using a light domain list. NO adult content.",
        "categories": ["security_light", "security_rules", "crypto"],
        "include_extra": False,
    },
    # --- ULTIMATE — the ONLY list with built-in porn blocking ---
    "persianshield-ultimate.txt": {
        "title": "PersianShield Ultimate (Complete + Adult)",
        "desc": "MAXIMUM protection: everything INCLUDING adult/porn blocking. HEAVY — includes large security and adult domain lists. This is the only list with built-in adult blocking.",
        "categories": ["persian", "ads", "privacy", "annoyances", "security_heavy", "security_rules", "crypto", "adult"],
        "include_extra": True,
    },
    # --- PORNLIST — standalone adult blocking (add on top of any list) ---
    "pornlist.txt": {
        "title": "PornList — Standalone Adult Blocking",
        "desc": "Standalone adult/pornography blocking list. Add this ON TOP of any other list (e.g., Light) to block adult content without using the heavy Ultimate list.",
        "categories": ["adult"],
        "include_extra": False,
    },
}

LOCALHOST_NAMES = {"localhost", "localhost.localdomain", "broadcasthost", "local", "ip6-localhost"}


def looks_like_ip(token):
    parts = token.split(".")
    return len(parts) == 4 and all(p.isdigit() for p in parts)


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
        if d in LOCALHOST_NAMES:
            return None
        return f"||{d}^"

    if len(parts) == 1:
        token = parts[0]
        is_bare_domain = (
            "##" not in token and "#" not in token and "$" not in token
            and "/" not in token and "|" not in token and "@" not in token
            and "*" not in token and "~" not in token and "^" not in token
            and "." in token and "://" not in token and not looks_like_ip(token)
        )
        if is_bare_domain:
            d = token.lower().rstrip(".")
            return f"||{d}^" if len(d) > 3 else None
        return token

    return line


def fetch(url):
    try:
        print(f"   ⬇️  {url}")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (PersianShield)"})
        with urllib.request.urlopen(req, timeout=40) as r:
            text = r.read().decode("utf-8", errors="ignore")
        return {p for ln in text.splitlines() if (p := parse_line(ln))}
    except Exception as e:
        print(f"   ⚠️  FAILED ({e})")
        return set()


def read_local_extra(path=LOCAL_EXTRA_FILE):
    if not os.path.exists(path):
        print(f"   ⚠️  '{path}' not found — skipping custom rules.")
        return set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        rules = {p for ln in text.splitlines() if (p := parse_line(ln))}
        print(f"   ✅ Loaded {len(rules):,} custom rules from {path}")
        return rules
    except Exception as e:
        print(f"   ⚠️  Error reading {path}: {e}")
        return set()


def human_size(nbytes):
    for unit in ("B", "KB", "MB", "GB"):
        if nbytes < 1024:
            return f"{nbytes:.1f} {unit}"
        nbytes /= 1024
    return f"{nbytes:.1f} TB"


def build_header(cfg, rule_count, size_bytes):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    ver = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    lines = ["[Adblock Plus 2.0]", f"! Title: {cfg['title']}"]
    for dl in cfg["desc"].split(". "):
        lines.append(f"! {dl.strip()}.")
    lines += [
        f"! Homepage: {HOMEPAGE}",
        "! Coded by: github.com/azadigh and t.me/azadi_tg",
        f"! Version: {ver}",
        f"! Last modified: {now}",
        "! Expires: 1 days (update frequency)",
        f"! Total rules: {rule_count:,}",
        f"! File size: {human_size(size_bytes)}",
        "! License: MIT",
        "!",
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
            lines.append(f"!   - {name}: {url}")
    lines.append("! ============================================================")
    lines.append("")
    return "\n".join(lines) + "\n"


def fetch_all_sources():
    cache = {}
    for cat, sources in SOURCES.items():
        cache[cat] = set()
        print(f"\n📂 Category: {CATEGORY_LABELS.get(cat, cat)}")
        for _, url in sources:
            cache[cat] |= fetch(url)
        print(f"   → {len(cache[cat]):,} rules cached")
    return cache


def write_file(filename, cfg, rules):
    sorted_rules = sorted(rules)
    body = "\n".join(sorted_rules) + "\n"
    size_bytes = len(body.encode("utf-8"))
    header = build_header(cfg, len(rules), size_bytes)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(body)
    return size_bytes, len(rules)


def main():
    print("🚀 PersianShield — building tiered filter lists...\n")

    cache = fetch_all_sources()
    extra = read_local_extra()

    print("\n" + "=" * 60)
    print("📦 Generating output files...")
    print("=" * 60)

    summary = []
    for filename, cfg in FILES.items():
        rules = set()
        for cat in cfg["categories"]:
            rules |= cache.get(cat, set())
        if cfg.get("include_extra", False):
            rules |= extra
        size, count = write_file(filename, cfg, rules)
        summary.append((filename, count, size))
        print(f"  ✅ {filename} — {count:,} rules — {human_size(size)}")

    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"{'File':<32} {'Rules':>12} {'Size':>10}")
    print("-" * 60)
    for filename, count, size in summary:
        print(f"{filename:<32} {count:>12,} {human_size(size):>10}")
    print("\n🎉 All lists generated successfully!")


if __name__ == "__main__":
    main()
