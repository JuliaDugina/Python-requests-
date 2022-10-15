import requests 
from bs4 import BeautifulSoup as bs

class HabrPythonNews:
    def __init__(self):
        self.url = https://habr.com/ru/hub/python/
        self.html = self.get_html()
        self.news = self.extract_python_news()


    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestsExeption, ValueError):
            print(“Server Error”)
            return False

    def extract_python_news(self):
        soup = BeautifulSoup(self.html, ‘html.parser’)
        news_list = soup.findAll(‘h2’, class_=’tm-article-snippet__title’)
        return news_list
n = HabrPythonNews()
for news in n.news:
    str_news = str(news)
    print(https://habr.com + str_next[136:str_news.find(‘”>span’)], news.find(‘span’).text)
print(n.news)
