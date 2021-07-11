# import csv
# from bs4 import BeautifulSoup 
# import requests,re
# # from urllib.request import urlopen
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError

# html =urlopen("https://www.bmw.in/en/footer/metanavigation/contact.html")
# soup = BeautifulSoup(html.content, 'lxml')

# with open("movieinfo.csv", 'w', newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(['name','year'])

#     for email in email_list:
#         # name = row.select_one(".browse-movie-title").text
#         # year = row.select_one(".browse-movie-year").text
#         writer.writerow([head,email])