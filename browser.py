from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Browser:
    def __init__(self):
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--headless")
        self._driver = webdriver.Chrome(options=chrome_options)
        self._last_update = None

    @property
    def last_update(self):
        return self._last_update

    # check for update
    def check(self, url):
        self._driver.get(url)
        update = self.__get_dom_text()
        if update != self._last_update:
            self._last_update = update
            return update
        return None

    def __get_dom_text(self):
        return self._driver.execute_script("return document.getElementsByTagName('body')[0].textContent").encode('utf-8')
    # close browser
    def dispose(self):
        if self._driver:
            try: self._driver.quit()
            except: pass