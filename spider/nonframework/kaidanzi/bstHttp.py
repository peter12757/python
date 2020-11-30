from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time
import os

bstUrl = "https://srm.shbst.com:8081/"

drivePath = "./spider/nonframework/kaidanzi/chromedriver"

class BstHttp():
    driver:WebDriver = None
    userName:str = ""
    userPassword:str = ""

    def __init__(self,name,password) -> None:
        self.driver = webdriver.Chrome(executable_path=drivePath)
        self.userName = name
        self.userPassword = password


    def login(self):
        self.driver.get(bstUrl)
        accountName = self.driver.find_element(By.ID,"txtJobNum")
        accountPwd = self.driver.find_element_by_id("txtPassword")
        loginBtn = self.driver.find_element_by_id("btnLogin")
        accountName.send_keys(self.userName)
        accountPwd.send_keys(self.userPassword)
        loginBtn.click()
        time.sleep(2)
        pass

    def selBeiEnKe(self):
        beienke = self.driver.find_element_by_id("rdbtnCompany_2")
        beienke.click()
        time.sleep(1)
        caigoudan = self.driver.find_element_by_id("XL_tvTreet4")
        caigoudan.click()
        time.sleep(1)
        unDeal =self.driver.find_element_by_id("ContentPlaceHolder1_ddlFalg")
        # 通过选项的value属性值来定位
        Select(unDeal).select_by_value("未处理")
        submit = self.driver.find_element_by_id("ContentPlaceHolder1_btnSCan")
        submit.click()
        time.sleep(1)

        pass

    def exit(self):
        """
        docstring
        """
        self.driver.close()
        pass

    


if __name__ == "__main__":
    http = BstHttp("S00186","589766")
    http.login()
    http.selBeiEnKe()
    time.sleep(10)
    http.exit()

    
    


        









