import urllib.request
import os
from datetime import datetime, timezone

REPO = os.getenv('GITHUB_REPOSITORY', 'yourusername/PersianShield')
HOMEPAGE = f"https://github.com/{REPO}"
LOCAL_EXTRA_FILE = "extra.txt"   # <-- your custom rules file

# ============================================================
# SOURCES (expanded with more comprehensive lists)
# ============================================================
SOURCES = {
    "ads_trackers": [
        ("EasyList", "https://easylist-downloads.adblockplus.org/easylist.txt"),
        ("EasyPrivacy", "https://easylist-downloads.adblockplus.org/easyprivacy.txt"),
        ("Peter Lowe's Ad/Tracking Server List", "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=0&mimetype=plaintext"),
        ("AdGuard Base filter", "https://filters.adtidy.org/extension/ublock/filters/2_optimized.txt"),
        ("AdGuard Tracking Protection", "https://filters.adtidy.org/extension/ublock/filters/3_optimized.txt"),
        ("AdGuard Mobile Ads", "https://filters.adtidy.org/extension/ublock/filters/11_optimized.txt"),
        ("AdGuard Experimental", "https://filters.adtidy.org/extension/ublock/filters/5.txt"),
        ("uBlock filters", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt"),
        ("uBlock - Privacy", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt"),
        ("uBlock - Unbreak", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt"),
        ("uBlock - Quick fixes", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt"),
    ],
    "annoyances": [
        ("EasyList Cookie List", "https://easylist-downloads.adblockplus.org/easylist-cookie.txt"),
        ("Fanboy's Annoyance List", "https://easylist-downloads.adblockplus.org/fanboy-annoyance.txt"),
        ("Fanboy's Social Blocking List", "https://easylist-downloads.adblockplus.org/fanboy-social.txt"),
        ("Fanboy's Notifications Blocking List", "https://easylist-downloads.adblockplus.org/fanboy-notifications.txt"),
        ("AdGuard Annoyances", "https://filters.adtidy.org/extension/ublock/filters/14_optimized.txt"),
        ("AdGuard Social Media", "https://filters.adtidy.org/extension/ublock/filters/4_optimized.txt"),
        ("uBlock - Annoyances", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt"),
    ],
    "security": [
        ("oisd full", "https://dbl.oisd.nl/"),
        ("StevenBlack unified hosts", "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"),
        ("uBlock - Badware risks", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt"),
        ("CoinBlockerLists", "https://raw.githubusercontent.com/ZeroDot1/CoinBlockerLists/master/list_browser.txt"),
        ("NoCoin (cryptomining)", "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt"),
        ("Dandelion Sprout's Anti-Malware List", "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout%27s%20Anti-Malware%20List.txt"),
        ("Spam404 malicious domains", "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt"),
    ],
    "persian": [
        ("PersianBlocker", "https://raw.githubusercontent.com/MasterKia/PersianBlocker/main/PersianBlocker.txt"),
        ("uBOPa", "https://raw.githubusercontent.com/nimasaj/uBOPa/master/uBOPa.txt"),
        ("AdBlock Iran", "https://raw.githubusercontent.com/farrokhi/adblock-iran/master/filter.txt"),
        ("AdBlockFA", "https://raw.githubusercontent.com/SlashArash/adblockfa/master/adblockfa.txt"),
        ("Persian Community List", "https://ideone.com/plain/K452p"),
    ],
    "porn": [
        ("oisd NSFW", "https://nsfw.oisd.nl/"),
        ("Chad Mayfield Porn Top1M", "https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list"),
        ("StevenBlack hosts (porn)", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts"),
    ],
}

LOCALHOST_NAMES = {"localhost", "localhost.localdomain", "broadcasthost", "local", "ip6-localhost"}


def looks_like_ip(token):
    parts = token.split(".")
    return len(parts) == 4 and all(p.isdigit() for p in parts)


def parse_line(line):
    """Normalize a line into an adblock rule. Returns None for comments/invalid."""
    line = line.strip()
    if not line:
        return None
    if line.startswith("!"):          # adblock comment
        return None
    if line.startswith("["):          # [Adblock Plus 2.0] header
        return None
    # hosts-style comment: '#' but NOT global cosmetic '##' nor exception '#@#'
    if line.startswith("#") and not line.startswith("##") and not line.startswith("#@"):
        return None

    parts = line.split()

    # hosts format: 0.0.0.0 domain / 127.0.0.1 domain
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
        return token  # already a valid adblock rule (cosmetic, exception, etc.)

    return line  # anything else, keep as-is


def fetch(url):
    try:
        print(f"   ⬇️  {url}")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (PersianShield)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            text = r.read().decode("utf-8", errors="ignore")
        return {p for ln in text.splitlines() if (p := parse_line(ln))}
    except Exception as e:
        print(f"   ⚠️  FAILED ({e})")
        return set()


def read_local_extra(path=LOCAL_EXTRA_FILE):
    """Read your custom extra.txt rules from the repository root."""
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


def build_header(title, desc_lines):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    ver = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    
    header = ["[Adblock Plus 2.0]", f"! Title: {title}"]
    header.extend(f"! {line}" for line in desc_lines)
    header.extend([
        f"! Homepage: {HOMEPAGE}",
        "! Coded by: github.com/azadigh and t.me/azadi_tg", # <-- YOUR CREDIT ADDED HERE
        f"! Version: {ver}",
        f"! Last modified: {now}",
        "! Expires: 1 days (update frequency)",
        "! License: MIT",
        "! ---------------------------------------------------------",
        "!",
    ])
    return "\n".join(header) + "\n"


def generate(filename, title, desc_lines, categories, extra_rules):
    print(f"\n🔨 Building {filename}...")
    all_rules = set()
    for cat in categories:
        print(f"  ➕ Category: {cat}")
        for _, url in SOURCES[cat]:
            all_rules |= fetch(url)
    all_rules |= extra_rules  # <-- merge YOUR custom extra.txt rules

    with open(filename, "w", encoding="utf-8") as f:
        f.write(build_header(title, desc_lines))
        f.write("\n".join(sorted(all_rules)))
        f.write("\n")
    print(f"  ✅ {len(all_rules):,} unique rules saved → {filename}")


def main():
    desc_common = [
        "Description: The ultimate, comprehensive adblock filter list.",
        "Once you subscribe, NO OTHER LIST IS REQUIRED. Blocks ads, trackers, malware,",
        "crypto-miners, cookie notices, social annoyances + deep Persian coverage.",
        "",
        "SOURCES USED (Citations & Credits):",
        "---------------------------------------------------------",
        "🌍 GLOBAL ADS & TRACKERS: EasyList, EasyPrivacy, Peter Lowe's,",
        "   AdGuard Base/Tracking/Mobile/Experimental, uBlock Origin core filters.",
        "🙅 ANNOYANCES: EasyList Cookie, Fanboy's Annoyance/Social/Notifications,",
        "   AdGuard Annoyances/Social, uBlock Annoyances.",
        "🛡️ SECURITY: oisd full, StevenBlack hosts, uBlock Badware,",
        "   CoinBlockerLists, NoCoin, Dandelion Sprout Anti-Malware, Spam404.",
        "🇮🇷 PERSIAN: PersianBlocker, uBOPa, AdBlock Iran, AdBlockFA, Community List.",
        "📝 CUSTOM: Includes additional hand-curated rules from this repo (extra.txt).",
        "---------------------------------------------------------",
    ]

    desc_family = desc_common + [
        "",
        "🔞 ADULT / PORNOGRAPHY BLOCKING (Family Safe):",
        "   oisd NSFW, Chad Mayfield Porn Top1M, StevenBlack porn extension.",
        "---------------------------------------------------------",
    ]

    # Load your custom rules ONCE, then merge into every final list
    extra_rules = read_local_extra(LOCAL_EXTRA_FILE)

    generate(
        "persianshield-ultimate.txt",
        "PersianShield Ultimate - The ONLY List You Need (No Ads, No Tracking)",
        desc_common,
        ["ads_trackers", "annoyances", "security", "persian"],
        extra_rules,
    )

    generate(
        "persianshield-family.txt",
        "PersianShield Family Safe - Ultimate + Adult Content Blocking",
        desc_family,
        ["ads_trackers", "annoyances", "security", "persian", "porn"],
        extra_rules,
    )


if __name__ == "__main__":
    main()
