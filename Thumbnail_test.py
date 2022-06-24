from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
import time
import fspath
import details
import pytest

class TestFibersafeDashboard():

 
    def pytest_html_report_title(report):
        ''' modifying the title  of html report'''
        reporttitle = 'report'+str(date.today)
        report.title = reporttitle

    @pytest.fixture(scope="session")
    def test_setup(self):
        global driver 
        global wait
        driver = webdriver.Chrome(ChromeDriverManager().install())
        wait = WebDriverWait(driver,10)
        driver.implicitly_wait(20)
        driver.maximize_window()
        yield
        print("Test Completed")
        driver.close()
        driver.quit()

    def test_login(self,test_setup):
        ##Development 
        # driver.get('https://fibersafe.tmrnd.com.my:84/portal/login')
        ##Production
        driver.get('https://patrol.tmrnd.com.my/portal/login')
        
        driver.find_element_by_id(fspath.Login.login_usrname).send_keys(details.NOCuser)
        driver.find_element_by_id(fspath.Login.login_pass).send_keys(details.Password)
        driver.find_element_by_xpath(fspath.Login.login_button).click()

    def test_worklist(self,test_setup):
        driver.find_element_by_xpath(fspath.Navigation.reportmenu).click()
        driver.find_element_by_xpath(fspath.Navigation.worklistnav).click()

        ##Load the listview
        try:
            loadList = wait.until(EC.presence_of_element_located((By.XPATH,fspath.Worklist.Listalert(1))))
            time.sleep(2)
            print('is ready')
        except TimeoutException:
            print("TimeOut, Please try again")
        
        time.sleep(2)
        driver.find_element_by_xpath(fspath.Worklist.toggleView).click()
        time.sleep(2)

        ## Load the Thumbnail view
        try:
            loadThumbnail = wait.until(EC.presence_of_element_located((By.XPATH,fspath.Worklist.Thumbnailalert(1))))
            print('is ready')
        except TimeoutException:
            print("TimeOut, Please try again")
        
    def test_filter(self,test_setup):
        time.sleep(2)
        driver.find_element_by_xpath(fspath.Worklist.filtericon).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(fspath.Worklist.filterstatus).click()
        driver.find_element_by_xpath(fspath.Worklist.inprogress).click()
        time.sleep(2)
        driver.find_element_by_xpath(fspath.Worklist.applyfilter).click()
        time.sleep(2)

        ##Load the listview
        try:
            loadList = wait.until(EC.presence_of_element_located((By.XPATH,fspath.Worklist.Listalert(1))))
            time.sleep(2)
            print('is ready')
        except TimeoutException:
            print("TimeOut, Please try again")
        
        driver.find_element_by_xpath(fspath.Worklist.toggleView).click()
        time.sleep(2)
        driver.find_element_by_xpath(fspath.Worklist.tndetail).click()
        time.sleep(2)
        driver.find_element_by_xpath(fspath.Inspectioninfo.backbutton).click()
        driver.refresh()
        time.sleep(2)

    # Due to limited dataset, need to remove invalid for awhile
    # def test_invalid(self,test_setup):
    #     time.sleep(3)
    #     driver.refresh()
    #     try:
    #         loadThumbnail = wait.until(EC.presence_of_element_located((By.XPATH,fspath.Worklist.Thumbnailalert(1))))
    #         time.sleep(2)
    #         print('is ready')
    #     except TimeoutException:
    #         print("TimeOut, Please try again")
    #     driver.implicitly_wait(10)
    #     driver.find_element_by_xpath(fspath.Worklist.tncheckbox).click()
    #     time.sleep(5)
    #     driver.find_element_by_xpath(fspath.Worklist.markinvalid).click()
    #     driver.implicitly_wait(10)
    
    def test_showmore(self,test_setup):
        time.sleep(2)
        driver.find_element_by_xpath(fspath.Worklist.showmore).click()
    
    def test_enlarge(self,test_setup):
        driver.find_element_by_xpath(fspath.Worklist.searchbar).send_keys('Dashcam')
        driver.find_element_by_xpath(fspath.Worklist.searchbtn).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Worklist.enlargeimg).click()
        time.sleep(3)
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        