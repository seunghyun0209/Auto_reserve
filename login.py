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
        self.dr ="";
        self.choice = 0;

    def choiceSite(self, site):
        print("===========================================");
        print("=============== choice Site ===============");
        print("1. 티켓링크 ");
        print("2. 인터파크 ");
        print("===========================================");

        self.choice = input();
        print(self.choice);
        site.setSiteValue(self.choice);

    def joinSite(self, site):
        self.dr = webdriver.Chrome('./chromedriver.exe')
        self.dr.get(site.getUrl());

    def loginSite(self, site, privateValue):
        if(self.choice == '1'):
            self.TicketLink_loginSite(site,privateValue);

    def TicketLink_loginSite(self, site, privateValue):

        login_elem =  self.dr.find_element_by_id(site.getLoginBtn());
        login_elem.click()
        self.dr.switch_to_window(self.dr.window_handles[1]);

        wait = WebDriverWait(self.dr, 10)
        id_elem = wait.until(EC.element_to_be_clickable((By.ID, site.getIdText())))
        pass_elem = self.dr.find_element_by_id(site.getPwText())
        id_elem.send_keys(privateValue.getId())
        pass_elem.send_keys(privateValue.getPw())
        login_elem = self.dr.find_element_by_id(site.getLoginBtn())
        login_elem.click()

        birth_elem = wait.until(EC.element_to_be_clickable((By.ID, site.getBirthText())))
        birth_elem.send_keys(privateValue.getBirthday())
        sec_login_elem = self.dr.find_element_by_id(site.getBirthBtn())
        sec_login_elem.click()

