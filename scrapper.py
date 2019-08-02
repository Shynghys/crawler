import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from datetime import datetime, timedelta
import csv


filename = "news.csv"
f = open(filename, "w")
headers = "news_name, story, published_date\n"
f.write(headers)


def get_single_item(item_url):
    bot = ureq(item_url)
    item_html = bot.read()
    bot.close()
    item_soup = soup(item_html, "html.parser")
    many_pages = item_soup.find_all('div', {"class": "fullnews white_block"})

    for one_page in many_pages:
        news_name = one_page.h1.text
        news_story = one_page.find_all("p", {"class": "description"})[0].text
        published_date = one_page.find_all("span", {"class": "news_date"})[0].text
        # like_votes = one_page.find_all("span", {"class": "rate_votes"})
        print(news_name)
        print(news_story)
        # print(like_votes)
        print(published_date)
        f.write(news_name + "," + news_story.replace(",", "|") + "," + published_date + "\n")


def web_crawler(max_pages):
    count = 0
    print("1")
    while count <= max_pages:
        print("2")
        d = datetime.today() - timedelta(days=count)
        d = d.strftime("%Y/%m/%d")
        my_url = 'https://www.zakon.kz/' + str(d)
        client = ureq(my_url)
        print("3")
        page_html = client.read()
        client.close()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("div", {"class": "cat_news_item"})

        for container in containers:
            print("4")
            for url_link in container.find_all('a', href=True):
                print("5")
                href = 'https://www.zakon.kz' + url_link['href']
                get_single_item(href)
        count += 1


web_crawler(1)
f.close()
