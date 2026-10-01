import asyncio
from pathlib import Path

from STRABERRY.utils.errors import capture_internal_err

COOKIE_PATH = Path("STRABERRY/assets/cookies.txt")


@capture_internal_err
async def fetch_and_store_cookies():
    """
    Cookies are DISABLED.
    Bot runs purely on APIs (Shruti Primary + Fallback API).
    This function just ensures an empty cookies file exists so
    any code that checks COOKIE_PATH doesn't crash.
    """
    try:
        COOKIE_PATH.parent.mkdir(parents=True, exist_ok=True)
        if not COOKIE_PATH.exists():
            COOKIE_PATH.write_text("# Netscape HTTP Cookie File\n", encoding="utf-8")
        print("ℹ️ Cookies disabled - bot running on API only.")
    except Exception as e:
        print(f"⚠️ Could not prepare cookies file (ignored): {e}")
    return None
