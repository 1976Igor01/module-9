from selenium.webdriver import ActionChains

def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Wait and click the element. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).\
                pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

menu = web_browser.find_element_by_css_selector(".nav")
hidden_submenu = web_browser.find_element_by_css_selector(".nav #submenu1")

ActionChains(web_browser).move_to_element(menu).click(hidden_submenu).perform()

menu = web_browser.find_element_by_css_selector(".nav")
hidden_submenu = web_browser.find_element_by_css_selector(".nav #submenu1")

actions = ActionChains(web_browser)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()

menu = web_browser.find_element_by_css_selector(".nav")
hidden_submenu = web_browser.find_element_by_css_selector(".nav #submenu1")

ActionChains(web_browser).move_to_element(menu).click(hidden_submenu).perform()
Или собраны в единую очередь и потом выполнены:

menu = web_browser.find_element_by_css_selector(".nav")
hidden_submenu = web_browser.find_element_by_css_selector(".nav #submenu1")

actions = ActionChains(web_browser)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()


def wait_for_animation(web_browser, selector):
    """
    Waits until jQuery animations have finished for the given jQuery  selector.
    """
    WebDriverWait(web_browser, 10).until(lambda web_browser: browser.execute_script(
        'return jQuery(%s).is(":animated")' % json.dumps(selector))
                                                             == False)


def wait_for_ajax_loading(web_browser, class_name):
    """
    Waits until the ajax loading indicator disappears.
    """
    WebDriverWait(web_browser, 10).until(lambda web_browser: len(web_browser.find_elements_by_class_name(
        class_name)) == 0)

def test_check_sort_by_price(web_browser):
    """ Проверка сортировки продуктов
    """

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()

    # Прокрутка до элемента, чтобы он стал виден пользователю
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Получение цен всех выведенных продуктов
    all_prices = page.products_prices.get_text()

    # Конвертирование всех цен из строк в числа
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() == 48

    # Проверяем наличие в названии слова iphone
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'iphone' in title.lower(), msg

from urllib.parse import urlparse

class BasePage(object):
   # конструктор класса - специальный метод с ключевым словом __init__
   # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов
   def __init__(self, driver, url, timeout=10):
       self.driver = driver
       self.url = url
       self.driver.implicitly_wait(timeout)


   def get_relative_link(self):
       url = urlparse(self.driver.current_url)
       return url.path

from selenium.webdriver.common.by import By

class AuthLocators:
   AUTH_EMAIL = (By.ID, "email")
   AUTH_PASS = (By.ID, "pass")
   AUTH_BTN = (By.CLASS_NAME, "btn-success")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "myDynamicElement"))
)

class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False
