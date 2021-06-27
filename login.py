from privateValue import privateValue
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import siteValue

class login(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        self.dr =""
        self.choice = 0
        self.concert = ""
        self.site = siteValue.site()
        self.privateValue = privateValue()

    def choiceSite(self):
        print("===========================================")
        print("=============== choice Site ===============")
        print("1. 티켓링크 ")
        print("2. 인터파크 ")
        print("===========================================")

        self.choice = input()
        print(self.choice)
        self.site.setSiteValue(self.choice)
        print("콘서트 정보 ")
        print("ex)http://www.ticketlink.co.kr/product/34880 중 product/34880")
        self.concert = "product/34880"



    def joinSite(self):
        self.dr = webdriver.Chrome('./chromedriver.exe')
        self.dr.get(self.site.getUrl())

    def loginSite(self):
        if(self.choice == '1'):
            self.TicketLink_loginSite()

    def TicketLink_loginSite(self):

        login_elem =  self.dr.find_element_by_id(self.site.getLoginBtn());
        login_elem.click()
        self.dr.switch_to_window(self.dr.window_handles[1]);

        wait = WebDriverWait(self.dr, 10)
        id_elem = wait.until(EC.element_to_be_clickable((By.ID, self.site.getIdText())))
        pass_elem = self.dr.find_element_by_id(self.site.getPwText())
        id_elem.send_keys(self.privateValue.getId())
        pass_elem.send_keys(self.privateValue.getPw())
        login_elem = self.dr.find_element_by_id(self.site.getLoginBtn())
        login_elem.click()

        birth_elem = wait.until(EC.element_to_be_clickable((By.ID, self.site.getBirthText())))
        birth_elem.send_keys(self.privateValue.getBirthday())
        sec_login_elem = self.dr.find_element_by_id(self.site.getBirthBtn())
        sec_login_elem.click()

    def selectReserveBtn(self):
        url = self.site.getUrl() +'product/34880'
        print("incoming selectReserveBtn func" + url)

        #date_elem = self.dr.find_element_by_class_name("btn reserve s_after first-child")
        #date_elem.click()

