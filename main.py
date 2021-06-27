import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib3.util import wait
import login
import siteValue
import privateValue


def loginfun(dr, my_id, my_pw, my_birth):
    dr.switch_to_window(dr.window_handles[1])
    print(dr.window_handles)
    print(my_id)
    print(my_pw)
    wait = WebDriverWait(dr, 10)
    id_elem = wait.until(EC.element_to_be_clickable((By.ID, "id")))
    pass_elem = dr.find_element_by_id("pw")
    id_elem.send_keys(my_id)
    id_elem.send_keys()
    pass_elem.send_keys(my_pw)
    login_elem = dr.find_element_by_id("loginBtn")
    login_elem.click()

    birth_elem = wait.until(EC.element_to_be_clickable((By.ID, "birthday")))
    birth_elem.send_keys(my_birth)
    sec_login_elem = dr.find_element_by_id("confirmBtn")
    sec_login_elem.click()

def inputPrivateData():
    m_privateData = privateValue.privateValue()
    print("===========================================")
    print("Input Your ID : ")
    m_privateData.setId("sunghyun020@naver.com")
    m_privateData.setPw("ae8824ae@")
    m_privateData.setBirthday("930209")
    return m_privateData

if __name__ == '__main__':
    m_login = login.login()
    m_site = siteValue.site()
    m_privateData = inputPrivateData()

    m_login.choiceSite()
    m_login.joinSite()
    m_login.loginSite()
    m_login.selectReserveBtn()




