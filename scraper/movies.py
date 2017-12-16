from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
import pymongo
import requests
import time
from pandas import DataFrame
import csv



def fetch_html(url):
    r= requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; \
        Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'})

    if r.status_code is not 200:
    	print("Error")
    else:
    	return r.text

def upcoming_movies(html_text, i, file):
 
    movie_dict={}

    soup=BeautifulSoup(html_text,"html.parser")
    name_span=soup.find_all("span",{"class":"trending-list-rank-item-name"})
    share_span=soup.find_all("span",{"class":"trending-list-rank-item-share"})
    local_time=time.time()
    for n in range(len(name_span)):
        movie_dict[n+1]={"name":name_span[n].getText(),"share":share_span[n].getText(), "time": local_time }
    #	movie_dict[n+1]={"name":name_span[n].getText(),"share + time":str(share_span[n].getText())+"|"+str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime((time.time()))))}
    
    #print(movie_dict)


    file = open("testfile2.csv","a")

    for keys in movie_dict:
        file.write(str(i)+","+movie_dict[keys]["name"]+","+str(movie_dict[keys]["share"])+","+str(movie_dict[keys]["time"])+"\n") 
      

    file.close()

if __name__=='__main__':
    i=1
    url="http://www.imdb.com/india/upcoming"
    file = open("testfile2.csv","w")
    file.write("id,name,share in %,time\n")
    file.close()

    while(True):
        
        html_text=fetch_html(url)
        upcoming_movies(html_text, i, file)
        i=i+1
        time.sleep(1800)


