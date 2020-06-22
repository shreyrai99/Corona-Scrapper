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
s = input('Enter name of country = ')
url2 = "https://www.worldometers.info/coronavirus/country/"
url2 = url2 + s
req2 = requests.get(url2)
soup2 = BeautifulSoup(req2.text,"html.parser")
data2 = soup2.find_all("div",class_ = "maincounter-number")
case2 = data2[0].text.strip()
death2 = data2[1].text.strip()
recover2 = data2[2].text.strip()
print(f"------{s} Corona Data-------")
print(f"Total cases = {case2}")
print(f"Total deaths = {death2}")
print(f"Total recovered patients = {recover2}")
