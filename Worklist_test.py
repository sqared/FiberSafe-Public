from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import random
import time
import fspath
import details
import pytest


class TestFibersafeWorklist():
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

# expand the bar
    def test_reports(self, test_setup):
        driver.find_element_by_xpath(fspath.Report.expand).click()
        time.sleep(3)

# view the worklist
    def test_worklist(self, test_setup):
        driver.find_element_by_xpath(fspath.Report.clickoption).click()
        time.sleep(3)

# ///////////////////////////////////////////////////// STATUS : UPCOMING //////////////////////////////////////////////////////////////////////#
# enter the status "UPCOMING" at the search box
    def test_searchstatusupcoming(self, test_setup):
        driver.find_element_by_xpath(fspath.Report.search1).send_keys("Upcoming")
        time.sleep(5)
# click the search button
        driver.find_element_by_xpath(fspath.Report.clicksearch).click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 2)
        choice2 = driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# back to the list of the worklist
        driver.find_element_by_xpath(fspath.Report.backbutton).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Report.search1).clear()

# ///////////////////////////////////////////////////// STATUS : IN PROGRESS //////////////////////////////////////////////////////////////////////#
# enter the status "IN PROGRESS" at the search box
    def test_searchstatusinprogress(self, test_setup):
        driver.find_element_by_xpath(fspath.Report.search1).send_keys("In progress")
        time.sleep(5)
# click the search button
        driver.find_element_by_xpath(fspath.Report.clicksearch).click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 2)
        choice2 = driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
# edit the field team member
    def test_selectfieldteammember1(self):
        driver.find_element_by_xpath(fspath.Report.edit).click()
        time.sleep(5)
#select any of the field team member name
        select1 = Select(driver.find_element_by_id("assignee_upd"))
        select1.select_by_visible_text("FT0002")
        time.sleep(5)
# enter the remark for the field team member
        driver.find_element_by_xpath(fspath.Report.remark).send_keys("Test")
        time.sleep(3)
# click "x" button
        driver.find_element_by_xpath(fspath.Report.clickcancel).click()
# set the date of visit
    def test_calendar_control_range1(self, test_setup):
        driver.find_element_by_xpath(fspath.Report.frame).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Report.year).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Report.month).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Report.day).click()
        time.sleep(5)
# save the changes
        driver.find_element_by_xpath(fspath.Report.save).click()
        time.sleep(5)

# update the status of inspection
    def test_updatestatus(self, test_setup):
# click the see details button
        driver.find_element_by_xpath(fspath.Report.seedetails).click()
        time.sleep(5)
# back to the inspection
        driver.find_element_by_xpath(fspath.Report.backbutton).click()
        time.sleep(3)
# back to the list of the worklist
        driver.find_element_by_xpath(fspath.Report.backbutton).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Report.search1).clear()

#///////////////////////////////////////////////////// STATUS : SUBMITTED //////////////////////////////////////////////////////////////////////#
# enter the status "SUBMITTED" at the search box
    def test_searchstatussubmitted(self, test_setup):
        driver.find_element_by_xpath(fspath.Report.search1).send_keys("Submitted")
        time.sleep(5)
# click the search button
        driver.find_element_by_xpath(fspath.Report.clicksearch).click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 1)
        choice2 = driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# click the see details button
        driver.find_element_by_xpath(fspath.Report.seedetails).click()
# scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
# edit the revisit
        driver.find_element_by_xpath(fspath.Report.editrevisit).click()
        time.sleep(5)
# click the require revisit
        driver.find_element_by_xpath(fspath.Report.require).click()
        time.sleep(5)

#set the date of visit
    def test_calendar_control_range2(self,test_setup):
        driver.find_element_by_xpath(fspath.Report.frame1).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Report.year1).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Report.month1).click()
        time.sleep(5)
        driver.find_element_by_xpath(fspath.Report.day1).click()
        time.sleep(5)
#click the submit button
        driver.find_element_by_xpath(fspath.Report.submit1).click()
        time.sleep(5)
# back to the inspection
        driver.find_element_by_xpath(fspath.Report.backbutton).click()
        time.sleep(3)
# back to the list of the worklist
        driver.find_element_by_xpath(fspath.Report.backbutton).click()
        time.sleep(3)
        # driver.find_element_by_xpath(fspath.Report.search1).clear()

# # ///////////////////////////////////////////////////// STATUS : DECLINE//////////////////////////////////////////////////////////////////////#
# # enter the status "DECLINE" at the search box
#     def test_searchstatusdecline(self, test_setup):
#         driver.find_element_by_xpath(fspath.Report.search1).send_keys("Decline")
#         time.sleep(5)
# # click the search button
#         driver.find_element_by_xpath(fspath.Report.clicksearch).click()
#         time.sleep(5)
# # choose any of the user from the list
#         driver.find_element_by_xpath(fspath.Report.choice).click()
# # edit the field team member
#     def test_selectfieldteammember3(self, test_setup):
#         driver.find_element_by_xpath(fspath.Report.edit).click()
#         time.sleep(5)
# # select any of the field team member name
#         select1 = Select(driver.find_element_by_id("assignee_upd"))
#         select1.select_by_visible_text("arfan FT 2")
#         time.sleep(5)
# # enter the remark for the field team member
#         driver.find_element_by_xpath(fspath.Report.remark).send_keys("Test")
#         time.sleep(5)
#
# #set the date of visit
#     def test_calendar_control_range3(self, test_setup):
#         driver.find_element_by_xpath(fspath.Report.frame).click()
#         time.sleep(5)
#         driver.find_element_by_xpath(fspath.Report.year).click()
#         time.sleep(5)
#         driver.find_element_by_xpath(fspath.Report.month).click()
#         time.sleep(5)
#         driver.find_element_by_xpath(fspath.Report.day).click()
#         time.sleep(5)
# # save the changes
#         driver.find_element_by_xpath(fspath.Report.save).click()
#         time.sleep(5)
# # back to the list of the worklist
#         driver.find_element_by_xpath(fspath.Report.backbutton).click()
#         time.sleep(5)
#         driver.find_element_by_xpath(fspath.Report.search1).clear()
#
# # ///////////////////////////////////////////////////// STATUS : INVALID //////////////////////////////////////////////////////////////////////#
# # enter the status "INVALID" at the search box
#     def test_searchstatusinvalid(self, test_setup):
#         driver.find_element_by_xpath(fspath.Report.search1).send_keys("Invalid")
#         time.sleep(5)
# # click the search button
#         driver.find_element_by_xpath(fspath.Report.clicksearch).click()
#         time.sleep(5)
# # choose any of the user from the list
#         i = random.randint(1, 10)
#         choice2 = driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
#         print(choice2)
#         choice2.click()
#         time.sleep(5)
# # back to the list of the worklist
#         driver.find_element_by_xpath(fspath.Report.backbutton).click()
#         time.sleep(5)
#         driver.find_element_by_xpath(fspath.Report.search1).clear()
#         time.sleep(10)

