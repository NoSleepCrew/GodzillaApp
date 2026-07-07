"""Load index.html in headless Chromium and verify the Phase 1 shell."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
URL = INDEX.as_uri()


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright not installed - skip smoke test or: pip install playwright && playwright install chromium")
        return 0

    errors = []
    logs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
        page.on("console", lambda msg: logs.append(f"{msg.type}: {msg.text}"))
        page.goto(URL, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(1500)

        checks = {
            "title": "Kaiju Quest" in page.title(),
            "dashboard": page.locator("#dashboard.active").count() == 1,
            "defenderLevel": page.locator("#defenderLevel").inner_text(timeout=5000) == "1",
            "rulebook": page.locator("#rulebook").count() == 1,
            "parent": page.locator("#parent").count() == 1,
            "syncInactive": "inactive" in page.locator("#syncStatus").inner_text(timeout=5000).lower(),
        }

        for screen_id in ["missions", "kaiju", "city", "rewards", "rulebook", "parent"]:
            page.locator(f"#nav-{screen_id}").click()
            page.wait_for_timeout(200)
            checks[f"screen_{screen_id}"] = page.locator(f"#{screen_id}.active").count() == 1

        page.evaluate(
            """() => {
          const before = state.energyPoints;
          state.energyPoints = before + 1;
          save();
          localStorage.setItem('kq_smoke_test', String(state.energyPoints));
        }"""
        )
        page.reload(wait_until="domcontentloaded")
        page.wait_for_timeout(1000)
        persisted = page.evaluate(
            """() => ({
          energy: state.energyPoints,
          smoke: localStorage.getItem('kq_smoke_test'),
          key: localStorage.getItem('kq_rpg_state') !== null
        })"""
        )
        checks["savePersist"] = persisted["energy"] == int(persisted["smoke"] or 0)
        checks["stateKey"] = persisted["key"]
        page.evaluate("localStorage.removeItem('kq_smoke_test')")

        browser.close()

    print("URL:", URL)
    for e in errors:
        print("ERROR:", e)
    for line in logs:
        if line.startswith("error:"):
            print(line)
    print("Checks:", checks)

    failed = errors or not all(checks.values())
    if failed:
        return 1
    print("smoke ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
