# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 14:40:42 2017

@author: Admin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from selenium.common.exceptions import NoSuchElementException
import time


def inputbox():
    pressed = False
    master = Tk()
    
    e = Entry(master)
    e.pack()
    
    e.focus_set()
    
    def callback():
        k = e.get()
        pressed = True
        master.destroy()
        
    
    b = Button(master, text="get", width=10, command=callback)
    b.pack()
    
    mainloop()
    if pressed:
        return k
    else:
        return ""
    
def getPosts(driver):
    return driver.find_elements_by_xpath('//*[contains(@id,"mall_post_")]')
    
  
    
def getText(post):   
    k= ""
    try:
        k = str(post.find_element_by_xpath('.//*[@class="_58jw"]').text)
        
    except NoSuchElementException:
        try:
           k = str(post.find_element_by_xpath('.//*[@class="_5pbx userContent"]').text)
        except NoSuchElementException:
            k="-1"
    return k
    
def commentPost(post,comment):
    inp = post.find_element_by_xpath('.//*[contains(@class,"_2xwx")]')
    inp.click()
    time.sleep(0.01)
    inp = post.find_element_by_xpath('.//*[contains(@class,"_2xwx")]//*[@role="combobox"]')
    inp.send_keys(comment+Keys.ENTER)
    
def CSP(driver,text,comment): # Comment Screened Post
    posts = getPosts(driver)
    for i in posts:
        k = getText(i)
        if text in k:
            commentPost(i,comment)
            return
            
def Chrome_FB(link="https://www.facebook.com"):
    coption = webdriver.ChromeOptions()
    coption.add_argument('user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data/Default/')
    
    browser = webdriver.Chrome(chrome_options = coption)
    
    browser.get(link)
    return browser #driver
    

    



browser = Chrome_FB()

inputbox()
print("kuy")

CSP(browser,"5730528021","Testing kub")

