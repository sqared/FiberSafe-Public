from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import fspath
import details
import pytest

class TestFibersafeMap():
    base_URL = "https://patrol.tmrnd.com.my/portal/login"

    @pytest.fixture(scope="session")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get(self.base_URL)
        driver.maximize_window()
        yield
        print("Test Completed")
        driver.close()
        driver.quit()

    def test_login(self, test_setup):
        driver.find_element_by_id(fspath.Login.login_usrname).send_keys(details.tenantuser)
        driver.find_element_by_id(fspath.Login.login_pass).send_keys(details.tenantpass)
        driver.find_element_by_xpath(fspath.Login.login_button).click()
        time.sleep(15)

# click the Map at Menu Bar
    def test_Map(self, test_setup):
        driver.find_element_by_xpath(fspath.Map.menubarmap).click()
        time.sleep(5)

# enter the address
    def test_searchaddress(self, test_setup):
        driver.find_element_by_xpath(fspath.Map.search).send_keys('TM CYBERJAYA TOWER, Cyberjaya, Selangor, Malaysia')
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Map.search).send_keys(Keys.ENTER)

# choose the cable type
    def test_cabletype(self,test_setup):
        driver.find_element_by_xpath(fspath.Map.clickbutton).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Map.clickbutton1).click()
        time.sleep(5)