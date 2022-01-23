import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/all/'

page = requests.get(url)


def get_article_link():
    try:
        article_head = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2")
        for tag in article_head:
            article_link = 'https://habr.com' + tag.attrs["href"]
    except:
        article_link = 'это мегапост, ссылка в другом теге'
    return article_link


def get_article_data():
    try:
        article_data_span = article.find(class_="tm-article-snippet__datetime-published")
        for tag in article_data_span:
            article_data = tag.attrs["title"]
    except:
        article_data = 'это мегапост, дата в другом теге'
    return article_data


def get_article_name():
    try:
        article_name = article.find(class_="tm-article-snippet__title-link").text
    except:
        article_name = 'это мегапост, заголовок в другом теге'
    return article_name


def is_article_good_enough():
    new_url = get_article_link()
    new_page = requests.get(new_url)
    new_soup = BeautifulSoup(new_page.text, features='html.parser')
    sub_article = new_soup.find('article')
    article_text = sub_article.find('div', class_="tm-article-body").text
    good_enough = 0
    for word in KEYWORDS:
        if article_text.lower().find(word) > 0:
            good_enough = 1
    if good_enough != 0:
        print(get_article_data(), get_article_name(),  get_article_link())
    return


soup = BeautifulSoup(page.text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    is_article_good_enough()

