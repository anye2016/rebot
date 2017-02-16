# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:10:36 2017

@author: anye2016
"""

import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.wise.xmu.edu.cn/people/faculty');
html = r.content;
soup = BeautifulSoup(html,'html.parser');
div_people_list = soup.find('div',attrs={'class':'people_list'})
a_s = div_people_list.find_all('a',attrs={'target':'_blank'})
for a in a_s:
    url = a['href']
    name = a.get_text()
    print name,url