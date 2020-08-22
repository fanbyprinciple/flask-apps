import pandas as pd 
from splinter import Browser 
from bs4 import BeautifulSoup 

executable_path = {'executable_path':'C:\Program Files\Mozilla Firefox/firefox.exe'}
browser = Browser('firefox', **executable_path, headless=False)

# get into the website
def grab_details():
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    print(soup)
