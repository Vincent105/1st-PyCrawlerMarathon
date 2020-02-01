import threading
import time
import requests
from bs4 import BeautifulSoup

startTime = time.time()

def run_1(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html5lib")

    for d in soup.find_all(class_="title"):
        print("標題:", d.text.replace('\t', '').replace('\n', ''))
        try:
            r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
            print('作者: ' + r.find(class_='article-meta-value').text)
        except:
            continue           
    print('Thread_1 stopped')


def run_2(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html5lib")

    for d in soup.find_all(class_="title"):
        print("標題:", d.text.replace('\t', '').replace('\n', ''))
        try:
            r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
            print('作者: ' + r.find(class_='article-meta-value').text)
        except:
            continue   
    print('Thread_2 stopped')


def main():
    t1 = threading.Thread(target=run_1, args=(
        'https://www.ptt.cc/bbs/Stock/index.html',))
    t2 = threading.Thread(target=run_2, args=(
        'https://www.ptt.cc/bbs/NBA/index.html',))
    t1.start()        
    t2.start()
    t1.join()
    t2.join()

    while True:
        length = len(threading.enumerate())
        if length <= 1:
            break
            
    finishTime = time.time()
    print('任務結束爬蟲擷取時間:', finishTime - startTime)  # 正常情況的爬蟲所需時間
    print('.py測試時間減少一半，ipynb無法顯示threading.enumerate()偵測數據')            

if __name__ == '__main__':
    main()