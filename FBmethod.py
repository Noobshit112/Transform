# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 14:40:42 2017

@author: Admin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import Tk,Entry,Button,mainloop
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
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
    
  
def getPoster(post):
    k = ""
    k = str(post.find_element_by_xpath('.//*[contains(@class,"_5pbw")]').text)
    return k

def getPastTime(post):
    k = ""
    k = str(post.find_element_by_xpath('.//*[contains(@class,"_5pcq")]').text)
    return k

def getTime(post):
    k = ""
    k = str(post.find_element_by_xpath('.//abbr[*]').get_attribute("title"))
    return k

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

def getComments(post):
    return post.find_elements_by_xpath('.//*[contains(@id,"comment_js")]')

def getCommenter(comment):
    k = ""
    k = str(comment.find_element_by_xpath('.//*[contains(@class,"UFICommentActorName")]').text)
    return k
    # UFICommentActorName
    
def getCommentText(comment):
    k = ""
    k = str(comment.find_element_by_xpath('.//span[contains(@data-ft,"K")]').text)
    return k
    
def commentPost(post,commentText):
    inp = post.find_element_by_xpath('.//*[contains(@class,"_2xwx")]')
    inp.click()
    time.sleep(0.01)
    inp = post.find_element_by_xpath('.//*[contains(@class,"_2xwx")]//*[@role="combobox"]')
    inp.send_keys(commentText+Keys.ENTER)
    
def CSP(driver,text,commentText): # Comment Screened Post
    posts = getPosts(driver)
    for i in posts:
        k = getText(i)
        if text in k:
            commentPost(i,commentText)
            return
            
def Chrome_FB(link="https://www.facebook.com"):
    coption = webdriver.ChromeOptions()
    coption.add_argument('user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data/Default/')
    
    browser = webdriver.Chrome(chrome_options = coption)
    
    browser.get(link)
    return browser #driver
    
def likePost(post):
    inp = post.find_element_by_xpath('.//*[contains(@class,"UFILikeLink _")]')
    inp.click()
    #UFILikeLink _4x9- _4x9_ _48-k
    #UFILikeLink UFIReactionLink
    
def likeComment(comment):
    inp = comment.find_element_by_xpath('.//*[contains(@class,"UFILikeLink")]')
    inp.click()
    
def getAllComments(post):
    found = False
    while found == False:
        try:
            k = post.find_element_by_xpath('.//*[@class="UFIPagerLink"]')      
        except NoSuchElementException:
            break
        k.click()
        time.sleep(0.1)
    return post.find_elements_by_xpath('.//*[contains(@id,"comment_js")]')
    #UFIPagerLink
    
    
    




# Get all Comment
#browser = Chrome_FB()
#
#inputbox()
#print("kuy")
#
#posts = getPosts(browser)
#for i in posts:
#    print("      " + getPoster(i)+ " --> " + getText(i))
#    comments = getAllComments(i)
#    for j in comments:
#        print(getCommenter(j) + " : " + getCommentText(j))