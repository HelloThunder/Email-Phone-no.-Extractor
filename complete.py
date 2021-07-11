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
import csv
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



save_excel = True #Change to "True" to save email into Excel

book = Workbook()
sheet = book.active


def start_scrape(page, name_the_file):

    print("\n\nWebpage is currently being scrapped... please wait...")
    scrape = BeautifulSoup(page, 'lxml')
    # head = scrape.find('H1')
    # print(head)
    scrape = scrape.get_text()
    
    phone_numbers = set(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", scrape)) #"set" removes duplicates
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", scrape))

    # nodupnumber = len(list(phone_numbers))
    # nodupemail = len(list(emails))

    # dupnumber = len(list(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", scrape))) 
    # dupemail = len(list(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", scrape)))

    # number_of_dup_number = int(dupnumber) - int(nodupnumber) 
    # number_of_dup_email = int(dupemail) - int(nodupemail)

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

    print("-----------------------------\n")

    if len(emails) == 0:
        print("No email address(es) found.")
        print("-----------------------------\n")
    else:
        count = 1
        for item in emails:
            print('Email address #' + str(count) + ': ' + item)
            count += 1

    if save_excel:
        for row in zip(email_list) :
             sheet.append(row)
            
        excel_file = (name_the_file + ".xlsx")
        book.save(excel_file) 
       
    # print("\nDuplicates have been removed from list.")
    # print("Total phone numbers: ", nodupnumber)
    # print("Total email addresses: ", nodupemail)
    # print("There were " + str(number_of_dup_number) + " duplicate phone numbers.")
    # print("There were " + str(number_of_dup_email) + " duplicate email addresses.")

    # if save_excel:
    #     print("\n\nData has been stored inside of an Excel spreadsheet named: "
    #           + excel_file + " in this directory: " + os.getcwd())
    #     mod_time = os.stat(excel_file).st_mtime
    #     print("\nCompleted at: " + str(datetime.fromtimestamp(mod_time)))
    #     print("\nSize of file: " + str(os.stat(excel_file).st_size) + " KB")
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# url="https://www.simplicant.com/blog/"

# # with open ('websites.text','r') as f:
# #     for line in f.read():
# #         urls += line

# #convert strings to list of URLs
# # urls  = list(filter(None,urls.split('\n')))

# #loop over URLs
# # for url in urls:
# if url:
#     #make HTTP requests to urls
#     name_the_file = "9"
#     try:
#         # url ="https://www.simplicant.com/blog/"
#         page = urlopen(url) 
#         # start_scrape(page,name_the_file) :::::::::::
#     except:
#         hdr = {'User-Agent': 'Mozilla/5.0'}
#         req = Request(url, headers=hdr)
#         page = urlopen(req)
#         # start_scrape(page, name_the_file)::::::::
#     # res = urlopen(url)
#     # start_scrape(res,'9')
#     # print('crawled base url: ',res.url)

#     #parse response 
#     content  = BeautifulSoup(page, "lxml")

#     # Extract Contact Data
#     # emails_h = re.findall("""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",content.get_text())
#     # print('\n EMAILS (Home) : ', emails_h)

#     #extracts contact link if available 
#     try:
#       contact  = content.find('a',text = re.compile('contact',re.IGNORECASE))['href']
#       print(contact)
#     #  if contact!='NoneType':
#       if 'http' in contact:
#         contact_url = contact
#       else:
#         #   print("NOt Ok")
#         contact_url = page.url[0:-1] + contact

#        #crawling contact URl recursively
#       name_the_file = "9"
#       try:
#         # url ="https://www.simplicant.com/blog/"
#         page = urlopen(contact_url) 
#         start_scrape(page,name_the_file)
#       except:
#         hdr = {'User-Agent': 'Mozilla/5.0'}
#         req = Request(contact_url, headers=hdr)
#         page = urlopen(req)
#         start_scrape(page, name_the_file)
#     #   res_contact  =urlopen(contact_url)
#     #   start_scrape(res_contact,'9')
#     #   contact_content = BeautifulSoup(res_contact.text,'lxml').get_text()
#     #   print('crawled contact url: ',res_contact.url)

#      # Extract Contact Data
#     #   emails_c = re.findall('(\w+@\w+\.\w+\.\w+)',contact_content)

#     #   print(re.findall(r'(\w+@\w+\.\w+\.\w+)',contact_content))

    
#     except Exception as e:
#         print(e)

# try:
#     html = urlopen("https://www.simplicant.com/blog/") 
# except HTTPError as e :
#     print(e)
# except URLError as e :
#     print("The server could not be found")
# else:
#     print("It worked")
def home(url):
    if save_excel:
        # name_the_file = input("Name the file you would like to save the data in (don't include .xlsx): ")
          name_the_file = "9"
    try:
        # url ="https://www.simplicant.com/blog/"
        page = urlopen(url) 
        start_scrape(page,name_the_file)
    except HTTPError as e :
        print(e)
        # hdr = {'User-Agent': 'Mozilla/5.0'}
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
        # name_the_file = input("Name the file you would like to save the data in (don't include .xlsx): ")
          name_the_file = "9"
    try:
        # url ="https://www.simplicant.com/blog/"
        import urllib.request
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
        # req = Request(url, headers=hdr)
        # page = urlopen(req)
        start_scrape(data, name_the_file)
        # page = urlopen(url) 
        # start_scrape(data,name_the_file)
        # hdr = {'User-Agent': 'Mozilla/5.0'}
        # user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

# url = "http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers"
# headers={'User-Agent':user_agent,} 
        import urllib.request
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        request=urllib.request.Request(url,None,hdr) #The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()
        # req = Request(url, headers=hdr)
        # page = urlopen(req)
        start_scrape(data, name_the_file)

def main():
    # url="https://www.bmw.in/en/index.html"
    try: 
       from googlesearch import search 
    except ImportError:  
       print("No module named 'google' found") 
  
    # to search 
    query = "'Blog' and 'Applicant tracking system'"
    pages =set()
    #  with open("1.html","w") as f:
    #      f.write("\n")
    for j in search(query, tld="co.in",lang='en', start=0,num=20, stop=20, pause=2): 
    # with open("1.html","a") as f:
    #  f.write(j+"\n")
      pages.add(j)
      print(j)
    print(len(pages))
    for url in pages:
      # ::::::::Home page
    #   url ="https://www.betterbuys.com/ats/blog/"
      print(url)
      if 'http' in url:
        home(url)
        try:
         content1 = urlopen(url)
         content = BeautifulSoup(content1,'lxml')
         try:
          contact=content.find(text = re.compile('Contact',re.IGNORECASE)).parent['href']
          print(contact)
          #  if contact!='NoneType':
          if 'http'  in contact:
            
            Contact(contact)
          else:
            # contact_url ='http:'+contact
            # Contact(contact_url)
            print("Contact Url error")
          #  contact_url = contact.url[0:-1] + contact
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
              #  if contact!='NoneType':
             if 'http'  in contact:
            
              Contact(contact)
             else:
             # contact_url ='http:'+contact
             # Contact(contact_url)
               print("Contact Url error")
             #  contact_url = contact.url[0:-1] + contact
            except Exception as e:
             print(e)
              # req = Request(url, headers=hdr)
              # page = urlopen(req)
            # start_scrape(data, name_the_file)
     #   else:
     #      print("Contact Url error in home ")
       # print(url)
       #:::::::::contact page

    # except Exception as e:
    #     print(e)



main()
# import urllib.request
# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

# url = "http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers"
# headers={'User-Agent':user_agent,} 

# request=urllib.request.Request(url,None,headers) #The assembled request
# response = urllib.request.urlopen(request)
# data = response.read()