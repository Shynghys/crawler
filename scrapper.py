import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.zakon.kz/news/'
print(my_url)
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "cat_news_item"})


def get_single_item(item_url):
    ubot = uReq(item_url)
    item_html = ubot.read()
    ubot.close()
    item_soup = soup(item_html, "html.parser")
    many_pages = item_soup.find_all('div', {"class": "fullnews white_block"})
    for one_page in many_pages:
        news_name_h1 = one_page.h1.text
        news_story = one_page.find_all("p", {"class": "description"})[0].text
        published_date = one_page.find_all("span", {"class": "news_date"})[0].text
        # like_votes = one_page.find_all("span", {"class": "rate_votes"})
        print(news_name_h1)
        print(news_story)
        # print(like_votes)
        print(published_date)


def web_crawler():
    for container in containers:
        for url_link in container.find_all('a', href=True):
            href = 'https://www.zakon.kz' + url_link['href']
            print(href)
            get_single_item(href)
    # datetime = datetime.now
    # for news_page in news_pages:
