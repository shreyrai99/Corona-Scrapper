import urllib
from bs4 import BeautifulSoup
import requests

#For World
url1 = "https://www.worldometers.info/coronavirus/"
req1 = requests.get(url1)
soup1 = BeautifulSoup(req1.text,"html.parser")
data1 = soup1.find_all("div",class_ = "maincounter-number")
case1 = data1[0].text.strip()
death1 = data1[1].text.strip()
recover1 = data1[2].text.strip()
print("------World Corona Data-------")
print(f"Total cases = {case1}")
print(f"Total deaths = {death1}")
print(f"Total recovered patients = {recover1}")
print("\n")

#For India
url2 = "https://www.worldometers.info/coronavirus/country/india/"
req2 = requests.get(url2)
soup2 = BeautifulSoup(req2.text,"html.parser")
data2 = soup2.find_all("div",class_ = "maincounter-number")
case2 = data2[0].text.strip()
death2 = data2[1].text.strip()
recover2 = data2[2].text.strip()
print("------India Corona Data-------")
print(f"Total cases = {case2}")
print(f"Total deaths = {death2}")
print(f"Total recovered patients = {recover2}")


#For Random Country
s = input('Enter name of country whose data you wannt to know = ')
url3 = "https://www.worldometers.info/coronavirus/country/"
url3 = url3 + s
req3 = requests.get(url3)
soup3 = BeautifulSoup(req3.text,"html.parser")
data3 = soup3.find_all("div",class_ = "maincounter-number")
case3 = data3[0].text.strip()
death3 = data3[1].text.strip()
recover3 = data3[2].text.strip()
print(f"------{s} Corona Data-------")
print(f"Total cases = {case3}")
print(f"Total deaths = {death3}")
print(f"Total recovered patients = {recover3}")



body = f'''World Data \n Total Cases = {case1} \n Total Deaths = {death1} \n Total Recovered = {recover1}  \n
India Data \n Total Cases = {case2} \n Total Deaths = {death2} \n Total Recovered = {recover2}
 \nCountry whose Data you Wanted to Know is {s} \n
{s} Data \n Total Cases = {case3} \n Total Deaths = {death3} \n Total Recovered = {recover3}
\nStay Safe, Stay Healthy!'''

import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = "Enter Local Host email here"
EMAIL_PASSWORD = "Enter the password via local environment"

contacts = ['x@gmail.com', 'y@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Corona Latest Updates by Shrey Rai'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

msg.set_content(body)




with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)