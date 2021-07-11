import requests
from bs4 import BeautifulSoup
import re
import csv
import json
import re
from urllib.request import urlopen, Request
import os
from datetime import datetime
from urllib.error import HTTPError
from urllib.error import URLError

from openpyxl import Workbook
from bs4 import BeautifulSoup
import urllib.request
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



save_excel = True #Change to "True" to save email into Excel

book = Workbook()
sheet = book.active


def start_scrape(page, name_the_file):

    print("\n\nWebpage is currently being scrapped... please wait...\n")
    scrape = BeautifulSoup(page, 'lxml')
    scrape = scrape.get_text()
    
    phone_numbers = set(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", scrape)) #"set" removes duplicates
    emails = set(re.findall(r"[A-Za-z0-9\._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", scrape))

    nodupnumber = len(list(phone_numbers))
    nodupemail = len(list(emails))

    dupnumber = len(list(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", scrape))) 
    dupemail = len(list(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", scrape)))

    number_of_dup_number = int(dupnumber) - int(nodupnumber) 
    number_of_dup_email = int(dupemail) - int(nodupemail)

    email_list = list(emails)
    phone_numbers = list(phone_numbers)

    if len(phone_numbers) == 0:
        print("No phone number(s) found.")

        print("-----------------------------\n")
    else:
        count = 1
        for item in phone_numbers:
            print("Phone number #" + str(count) + ': ' + item)
            count += 1
    print("-----------------------------")

    if len(emails) == 0:
        print("No email address(es) found.")
        print("-----------------------------")
    else:
        count = 1
        for item in emails:
            print('Email address #' + str(count) + ': ' + item)
            count += 1
        print("\n::::::::::::::::::::::::::::::")
        print("::::::::::::::::::::::::::::::\n")
        # print("::::::::::::::::::::::::::::::\n")
    if save_excel:
        for row in zip(email_list) :
             sheet.append(row)
            
        excel_file = (name_the_file + ".xlsx")
        book.save(excel_file) 
       
    print("\nDuplicates have been removed from list.")
    print("Total phone numbers: ", nodupnumber)
    print("Total email addresses: ", nodupemail)
    print("There were " + str(number_of_dup_number) + " duplicate phone numbers.")
    print("There were " + str(number_of_dup_email) + " duplicate email addresses.")

    if save_excel:
        print("\n\nData has been stored inside of an Excel spreadsheet named: "
              + excel_file + " in this directory: " + os.getcwd())
        mod_time = os.stat(excel_file).st_mtime
        print("\nCompleted at: " + str(datetime.fromtimestamp(mod_time)))
        print("\nSize of file: " + str(os.stat(excel_file).st_size) + " KB")
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


def home(url):
    if save_excel:
          name_the_file = "9"
    try:
        page = urlopen(url) 
        start_scrape(page,name_the_file)
    except HTTPError as e :
        print(e)
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        req = Request(url, headers=hdr)
        page = urlopen(req)
        start_scrape(page, name_the_file)

def Contact(url):
    if save_excel:
          name_the_file = "9"
    try:
       
        page = urlopen(url) 
        start_scrape(page,name_the_file)
    except HTTPError as e :
        print(e)
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        request=urllib.request.Request(url,headers=hdr) #The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()
        start_scrape(data, name_the_file)
        
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        request=urllib.request.Request(url,None,hdr) #The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()
        start_scrape(data, name_the_file)

def main():
    
    try: 
       from googlesearch import search 
    except ImportError:  
       print("No module named 'google' found") 
  
    # to search 
    query = "'Blog' and 'Applicant tracking system'"
    pages =set()
    
    for j in search(query, tld="co.in",lang='en', start=0,num=30, stop=30, pause=2): 
      pages.add(j)
      print(j)
    print(len(pages))
    print(":::::::::::::::::::\n")
    for url in pages:

      # ::::::::Home page
      print(url)
      if 'http' in url:
        home(url)
        try:
         content1 = urlopen(url)
         content = BeautifulSoup(content1,'lxml')
         try:
          contact=content.find(text = re.compile('Contact',re.IGNORECASE)).parent['href']
          print(contact)
         
          if 'http'  in contact:
            
            Contact(contact)
          else:
            print("Contact Url error")

         except Exception as e:
            print(e)
        except HTTPError as e :
            print(e) 
            import urllib.request
            hdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
             'Accept-Encoding': 'none',
             'Accept-Language': 'en-US,en;q=0.8',
             'Connection': 'keep-alive'}
            request=urllib.request.Request(url,None,hdr) #The assembled request
            response = urlopen(request)
            data = BeautifulSoup(response,"lxml")
            try:
             contact=data.find('a',text = re.compile('Contact',re.IGNORECASE))['href']
             print(contact)
              
             if 'http'  in contact:
              Contact(contact)
             else:
               print("Contact Url error")
             
            except Exception as e:
             print(e)
              


main()
