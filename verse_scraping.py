import json

from playwright.sync_api import sync_playwright

URL = "https://quran.com/daily"


def scrape_daily_verse():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(URL, wait_until="domcontentloaded", timeout=60000)

        # Wait for dynamically loaded verse
        widget = page.locator('[data-testid="quran-widget"]')

        widget.wait_for(state="visible", timeout=60000)

        copy_data = widget.get_attribute("data-copy-data")

        if not copy_data:
            raise Exception("Daily verse data was not found.")  # noqa: TRY002

        data = json.loads(copy_data)

        verse = data["verses"][0]

        arabic_text = verse["arabicText"]
        translation = verse["translations"][0]["text"]

        verse_block = page.locator('[data-verse-block="true"]').first

        surah_name = verse_block.get_attribute("data-surah-name")

        verse_key = verse_block.get_attribute("data-verse-key")

        browser.close()

        return {"surah": surah_name,
            "verse": verse_key,
            "english": translation,
            "arabic":arabic_text
        }
