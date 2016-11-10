# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
GMAIL_ADRESS = "frabro568@gmail.com"
GMAIL_PASS = "ndagmabry9"


class Gmail:
    def __init__(self,gmail_adress,gmail_pass):
        #page1
        self.driver = webdriver.Chrome()
        self.driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/&hl=ja")
        elem = self.driver.find_element_by_css_selector('#Email')
        elem.send_keys(gmail_adress)
        elem = self.driver.find_element_by_css_selector('#next').click()
        sleep(0.5)
        elem = self.driver.find_element_by_css_selector('#Passwd')
        elem.send_keys(gmail_pass)
        sleep(0.5)
        elem = self.driver.find_element_by_css_selector('#signIn').click()
        sleep(3)

    def close(self):
        self.driver.close()

    def getPinCode(self):
        sleep(2)
        elems = self.driver.find_elements_by_css_selector('span')
        for e in elems:
            if e.text == '40404':
                e.click()
                sleep(5)
                break
        elems = self.driver.find_element_by_css_selector('body')
        pin_code = ""
        print('text is ',elems.text)
        if(isinstance(elems.text, unicode)):
            text = elems.text.encode('utf-8')

        print(type(elems.text))
        pattern = r"Twitter認証コードは([0-9]*)です"
        repatter = re.compile(pattern)
        matchOB = repatter.findall(text)
        print(matchOB)
        if len(matchOB) > 0:
            print("コード is:",matchOB[-1])
            pin_code = matchOB[-1]
        return pin_code
    # self.driver.switch_to_window(driver.window_handles[-1])

if __name__ == '__main__':
    gm = Gmail(gmail_adress=GMAIL_ADRESS,gmail_pass=GMAIL_PASS)
    print(gm.getPinCode())
