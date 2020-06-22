from flask import Flask,render_template,request
app = Flask(__name__)
#For World 
import urllib
from bs4 import BeautifulSoup
import requests
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = "https://www.worldometers.info/coronavirus/"
req1 = requests.get(url1)
soup1 = BeautifulSoup(req1.text,"html.parser")
data1 = soup1.find_all("div",class_ = "maincounter-number")
case1 = data1[0].text.strip()
death1 = data1[1].text.strip()
recover1 = data1[2].text.strip()

#For India
url2 = "https://www.worldometers.info/coronavirus/country/india/"
req2 = requests.get(url2)
soup2 = BeautifulSoup(req2.text,"html.parser")
data2 = soup2.find_all("div",class_ = "maincounter-number")
case2 = data2[0].text.strip()
death2 = data2[1].text.strip()
recover2 = data2[2].text.strip()


#For Unites States
url3 = "https://www.worldometers.info/coronavirus/country/us/"
req3 = requests.get(url3)
soup3 = BeautifulSoup(req3.text,"html.parser")
data3 = soup3.find_all("div",class_ = "maincounter-number")
case3 = data3[0].text.strip()
death3 = data3[1].text.strip()
recover3 = data3[2].text.strip()


@app.route('/')
def index():            
    return render_template("index.html",case1 = case1,death1=death1,recover1=recover1)

@app.route("/home")
def index3():
    return render_template("home.html")  

@app.route("/india")
def index1():
    return render_template("index1.html",case2 = case2,death2=death2,recover2=recover2)

@app.route('/US')
def index2():
   return render_template("index2.html",s="United States",case3 = case3,death3=death3,recover3=recover3)

@app.route("/<string:s>")
def index4(s):    
    url3 = "https://www.worldometers.info/coronavirus/country/"
    url3 = url3 + s
    s = s.capitalize()
    req3 = requests.get(url3)
    soup3 = BeautifulSoup(req3.text,"html.parser")
    data3 = soup3.find_all("div",class_ = "maincounter-number")
    case3 = data3[0].text.strip()
    death3 = data3[1].text.strip()
    recover3 = data3[2].text.strip()
    return render_template("index2.html",s=s,case3 = case3,death3=death3,recover3=recover3)
    

if __name__ == "__main__":
    app.run(debug=False)

