# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:07:40 2019

@author: Sammu
"""

import pandas as pd
from selenium import webdriver
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area" 
driver = webdriver.Chrome("C:/Users/Sammu/Desktop/ML/chromedriver.exe")

driver.get(url)   


right_table=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]')