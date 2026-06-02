'''
real world example - multithreading for I/o Tasks
Scene - web scraping
web scraping often involves making number of requests to fetch web pages .
Thse tasks are IO bound as they spend a lot of 
time waiting for response from servers.Multithreading can significanlt
improve the performane by allowing web page to be fetched concurrently 


https://www.imdb.com/title/tt2575988/
'''
import threading
import requests
from bs4 import BeautifulSoup
urls = ['https://en.wikipedia.org/wiki/Kumail_Nanjiani','https://exams.ntaonline.in/CUET-PG/',
        'https://www.imdb.com/title/tt2575988/']
def fetch_cont(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    print(f"fetched {soup.text} for {url}")

threadrs =[]
for url in urls:
    thread = threading.Thread(target=fetch_cont,args=(url,))
    threadrs.append(thread)
    thread.start()
for i in threadrs:
    i.join()
print("all web pages fetched")