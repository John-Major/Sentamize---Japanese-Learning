from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from asgiref.sync import sync_to_async

def index(request):
    
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
  

    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
    #driver.maximize_window()

    driver.get(f'https://jisho.org/search/goodbye')
    testing = driver.find_element_by_xpath('//*[@id="primary"]/div[1]/div[1]/div[1]/div[1]/div/span[2]')
    testing2 = driver.find_element_by_xpath('//*[@id="primary"]/div[1]/div[1]/div[2]/div/div/div/span[2]')

    response = "Word: " + testing.text +"   Meaning: " + testing2.text 
    return  HttpResponse(response)