from os import remove
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time
from module import *
import json

bstUrl = "https://srm.shbst.com:8081/"

drivePath = "./spider/nonframework/kaidanzi/chromedriver.exe"

class BstHttp(): 
    driver:WebDriver = None
    userName:str = ""
    userPassword:str = ""
    sleepTime:float = 0.5 
    httpOrderForm:[] = []

    def __init__(self,name,password) -> None:
        self.driver = webdriver.Chrome(executable_path=drivePath)
        self.userName = name
        self.userPassword = password


    def login(self):
        """
        登录贝斯特
        """
        self.driver.get(bstUrl)
        accountName = self.driver.find_element(By.ID,"txtJobNum")
        accountPwd = self.driver.find_element_by_id("txtPassword")
        loginBtn = self.driver.find_element_by_id("btnLogin")
        accountName.send_keys(self.userName)
        accountPwd.send_keys(self.userPassword)
        loginBtn.click()
        time.sleep(1)
        pass

    def selBeiEnKe(self):
        """
        查询对应的采购单
        """
        beienke = self.driver.find_element_by_id("rdbtnCompany_2")
        beienke.click()
        time.sleep(self.sleepTime)
        caigoudan = self.driver.find_element_by_id("XL_tvTreet4")
        caigoudan.click()
        time.sleep(self.sleepTime)
        unDeal =self.driver.find_element_by_id("ContentPlaceHolder1_ddlFalg")
        # 通过选项的value属性值来定位
        Select(unDeal).select_by_value("未处理")
        submit = self.driver.find_element_by_id("ContentPlaceHolder1_btnSCan")
        submit.click()
        time.sleep(self.sleepTime)
        pass


    def collectTableData(self):
        """
        docstring
        """
        table = self.driver.find_element_by_id("ContentPlaceHolder1_gvOrderView")
        table_row = table.find_elements_by_tag_name("tr")
        del table_row[0]
        index = len(table_row)
        print(str(index)+" need to collect")
        for i in range(index):
            table = self.driver.find_element_by_id("ContentPlaceHolder1_gvOrderView")
            table_row = table.find_elements_by_tag_name("tr")
            del table_row[0]
            self.fillTableFirstData(table_row[0])




    def fillTableFirstData(self, row):
        """
        docstring
        """
        items = row.find_elements_by_tag_name("td")
        item = HttpOrderForm(items[0].text,items[1].text,items[2].text,items[3].text,items[5].text)
        self.httpOrderForm.append(item)
        print = self.driver.find_element_by_id("ContentPlaceHolder1_gvOrderView_hkPrint_0")
        print.click()
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.fillDetailData(item)
        self.printOrder(item)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])


    def fillDetailData(self, order:HttpOrderForm):
        """
        docstring
        """
        tbody = self.driver.find_element_by_xpath('//div/table/tbody')
        items = tbody.find_elements_by_tag_name('tr')
        itemsNum = len(items)
        print("总共有几行："+str(itemsNum))
        orderDeatainum = itemsNum - 20
        print("单子有几项："+str(orderDeatainum))
        for index in range(13,orderDeatainum+13):
            item = self.driver.find_element_by_xpath("/html/body/form/div[3]/span/div/table/tbody/tr["+str(index)+"]")
            detailTD = item.find_elements_by_tag_name("td")
            orderDetail = XmlOrderForm(order.caigouNo,self.getgongzuoling(detailTD[6].text),
            detailTD[16].text,
            self.getxinghao(detailTD[2].text)+":"+detailTD[4].text,
            detailTD[10].text,
            detailTD[13].text)
            order.detailinfo.append(orderDetail)
        print(order)


    def getgongzuoling(self,gongzuoling:str):
        """
        docstring
        """
        if gongzuoling == '天津':
            return gongzuoling
        else:
            return ''


    def getxinghao(self, xinghao:str):
        """
        docstring
        """
        return xinghao



    def printOrder(self, order:HttpOrderForm):
        """
        docstring
        """
        # printBtn = self.driver.find_element_by_xpath('//*[@id="webRpt"]/table/tbody/tr[2]/td[6]/input')
        # order.
        # printBtn.click()
        pass



    def exit(self):
        """
        docstring
        """
        for tab in self.driver.window_handles:
            self.driver.close()
            time.sleep(1)
        pass

    


if __name__ == "__main__":
    http = BstHttp("S00186","589766")
    http.login()
    http.selBeiEnKe()
    http.collectTableData()
    data = {'data':http.httpOrderForm}
    jsonStr = json.dumps(data,default=lambda o: o.__dict__)
    with open("./record.json","w") as f:
        f.write(jsonStr)
    # time.sleep(1)
    # http.exit()
    while True:
        time.sleep(1)

    
    


        









