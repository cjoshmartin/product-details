from playwright.sync_api import sync_playwright

from main import amazon
from main import bose

parsers = [amazon, bose]


class Details:
    def __init__(self, headless=True):
        self.playwright = sync_playwright().start()
        iphone_11 = self.playwright.devices['iPhone 11 Pro']
        self.browser = self.playwright.webkit.launch(headless=headless)
        self.context = self.browser.new_context(**iphone_11)
        self.page = self.context.new_page()

    def get_metadata(self, url):
        for parser in parsers:
            if parser.matcher(url):
                return parser.get_meta_data(self.page, url)

        return {}

    def __del__(self):
        self.browser.close()
        self.playwright.stop()

# if __name__ == '__main__':
#