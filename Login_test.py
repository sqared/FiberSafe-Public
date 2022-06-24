from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
import time
import fspath
import details
import pytest


class TestFibersafeLogin():
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

#set the username
    def test_setusername(self, test_setup):
        driver.find_element_by_id(fspath.Login.login_usrname).send_keys(details.tenantuser)
        time.sleep(3)

#set the password
    def test_setpassword(self, test_setup):
        driver.find_element_by_id(fspath.Login.login_pass).send_keys(details.tenantpass)
        time.sleep(3)
#click the login button
    def test_clicklogin(self, test_setup):
        driver.find_element_by_xpath(fspath.Login.login_button).click()
        time.sleep(3)
