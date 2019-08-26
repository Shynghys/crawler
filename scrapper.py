from urllib.request import urlopen as ureq
from urllib.request import Request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as soup
from datetime import datetime, timedelta
from urllib.error import HTTPError, URLError
import random

filename = "news.csv"
f = open(filename, "w")
headers = "comments_number, news_name, story, published_date, time, news_author\n"
f.write(headers)
proxies = [{'ip': '177.105.192.126', 'port': '55715'}, {'ip': '195.91.249.211', 'port': '54698'},
           {'ip': '185.132.179.108', 'port': '1080'}, {'ip': '197.254.4.130', 'port': '57610'},
           {'ip': '83.228.74.251', 'port': '50800'}, {'ip': '91.139.1.158', 'port': '37504'},
           {'ip': '119.161.98.131', 'port': '3128'}, {'ip': '103.250.166.12', 'port': '47031'},
           {'ip': '191.100.24.251', 'port': '21776'}, {'ip': '158.69.138.15', 'port': '8080'},
           {'ip': '185.132.133.196', 'port': '1080'}, {'ip': '114.199.110.58', 'port': '47428'},
           {'ip': '46.0.203.186', 'port': '8080'}, {'ip': '144.217.229.153', 'port': '1080'},
           {'ip': '192.99.191.235', 'port': '1080'}, {'ip': '91.191.250.142', 'port': '60104'},
           {'ip': '2.188.164.58', 'port': '8080'}, {'ip': '103.94.120.66', 'port': '40096'},
           {'ip': '1.179.206.161', 'port': '31103'}, {'ip': '78.30.202.110', 'port': '60882'},
           {'ip': '192.227.237.110', 'port': '3128'}, {'ip': '178.217.168.77', 'port': '37427'},
           {'ip': '212.56.218.90', 'port': '30055'}, {'ip': '176.31.69.177', 'port': '8080'},
           {'ip': '103.137.7.162', 'port': '23500'}, {'ip': '187.191.20.7', 'port': '54375'},
           {'ip': '36.89.185.219', 'port': '53281'}, {'ip': '89.239.25.7', 'port': '31964'},
           {'ip': '37.200.224.179', 'port': '8080'}, {'ip': '103.100.79.17', 'port': '48515'},
           {'ip': '178.151.205.154', 'port': '61902'}, {'ip': '80.28.243.202', 'port': '52267'},
           {'ip': '181.40.18.66', 'port': '80'}, {'ip': '183.88.195.96', 'port': '8080'},
           {'ip': '202.154.234.123', 'port': '8080'}, {'ip': '95.168.185.183', 'port': '8080'},
           {'ip': '211.244.224.130', 'port': '8080'}, {'ip': '185.108.141.49', 'port': '8080'},
           {'ip': '177.46.149.22', 'port': '32884'}, {'ip': '78.110.154.177', 'port': '59888'},
           {'ip': '190.220.1.173', 'port': '48213'}, {'ip': '202.57.35.74', 'port': '47796'},
           {'ip': '41.190.92.99', 'port': '59192'}, {'ip': '80.255.91.38', 'port': '44177'},
           {'ip': '138.219.44.213', 'port': '8080'}, {'ip': '180.180.156.60', 'port': '58169'},
           {'ip': '84.52.85.235', 'port': '40749'}, {'ip': '110.74.222.159', 'port': '40348'},
           {'ip': '134.119.188.147', 'port': '8080'}, {'ip': '186.211.106.227', 'port': '34334'},
           {'ip': '87.120.145.59', 'port': '53281'}, {'ip': '190.184.144.146', 'port': '50145'},
           {'ip': '138.97.12.150', 'port': '32612'}, {'ip': '181.39.86.234', 'port': '8080'},
           {'ip': '154.41.2.154', 'port': '13538'}, {'ip': '177.99.206.82', 'port': '8080'},
           {'ip': '62.122.201.241', 'port': '46176'}, {'ip': '77.246.54.97', 'port': '80'},
           {'ip': '113.11.47.242', 'port': '40071'}, {'ip': '180.232.77.107', 'port': '49149'},
           {'ip': '170.84.93.73', 'port': '36001'}, {'ip': '202.57.54.153', 'port': '36499'},
           {'ip': '185.132.178.133', 'port': '1080'}, {'ip': '83.171.114.92', 'port': '36307'},
           {'ip': '14.102.44.1', 'port': '44047'}, {'ip': '103.137.66.2', 'port': '8080'},
           {'ip': '114.199.115.244', 'port': '38509'}, {'ip': '103.74.220.47', 'port': '59000'},
           {'ip': '180.87.195.22', 'port': '44997'}, {'ip': '41.190.95.92', 'port': '47720'},
           {'ip': '42.112.21.221', 'port': '3128'}, {'ip': '180.211.193.74', 'port': '40536'},
           {'ip': '46.99.163.166', 'port': '8080'}, {'ip': '176.215.255.190', 'port': '57068'},
           {'ip': '77.39.7.153', 'port': '38264'}, {'ip': '170.246.85.38', 'port': '55973'},
           {'ip': '217.182.51.226', 'port': '8080'}, {'ip': '192.140.42.28', 'port': '39653'},
           {'ip': '46.246.88.6', 'port': '8118'}, {'ip': '103.107.133.29', 'port': '43683'},
           {'ip': '95.87.14.47', 'port': '45522'}, {'ip': '186.125.59.8', 'port': '44811'},
           {'ip': '159.255.167.28', 'port': '53584'}, {'ip': '178.168.19.139', 'port': '30736'},
           {'ip': '181.189.221.245', 'port': '42407'}, {'ip': '51.158.106.54', 'port': '8811'},
           {'ip': '54.39.53.104', 'port': '3128'}, {'ip': '51.158.119.88', 'port': '8811'},
           {'ip': '51.38.71.101', 'port': '8080'}, {'ip': '196.37.143.202', 'port': '8080'},
           {'ip': '134.119.205.167', 'port': '8080'}, {'ip': '185.132.178.140', 'port': '1080'},
           {'ip': '104.248.152.243', 'port': '8080'}, {'ip': '51.158.98.121', 'port': '8811'},
           {'ip': '198.98.51.240', 'port': '8080'}, {'ip': '182.48.80.23', 'port': '8080'},
           {'ip': '201.151.79.30', 'port': '8080'}, {'ip': '204.29.115.149', 'port': '8080'},
           {'ip': '92.222.94.78', 'port': '3128'}]
ua = UserAgent()


def get_single_item(item_url):
    bot = ureq(item_url)
    item_html = bot.read()
    bot.close()
    item_soup = soup(item_html, "html.parser")
    another_pages = item_soup.find_all('div', {"class": "clear_floats"})
    many_pages = item_soup.find_all('div', {"class": "fullnews white_block"})
    print("many")

    print(
        "777777777777777777777777777777777777777777777777777"
        "77777777777777777777777777777777777777777777777")

    print(another_pages)
    if many_pages:
        print("5")
        for one_page in many_pages:
            news_name = one_page.h1.text.replace(",", "/")
            print("6")
            news_story = one_page.find_all("p", {"class": "description"})[0].text.replace('""', '|')
            published_date = one_page.find_all("span", {"class": "news_date"})[0].text
            f.write("," + news_name.replace('""', '/') + "," + news_story.replace(",", "/") + ","
                    + published_date + "\n")
    elif another_pages:
        # another_pages = item_soup.find_all('div', {"class": "news_area"})
        print(
            "55555555555555555555555555555555555555555555555555555555555555555"
            "5555555555555555555555555555555555555555555555555555")
        print("another_pages")
        print("5555555555555555555555555555555555555555555555555555")
        print("many_pages")
        print(
            "55555555555555555555555555555555555555555555555555555555555"
            "5555555555555555555555555555555555555555555555555555555555")
        for another_one_page in another_pages:
            news_name = another_one_page.find_all("span", {"class": "s0"})[0].text
            print("666666666")

            news_story = another_one_page.find_all("span", {"class": "s1"})[0].text.replace('""', '|')
            published_date = another_one_page.find_all("div", {"class": "news_date"})[0].text
            news_author = another_one_page.find_all("span", {"class": "s0"})[-1].text.replace('""', '|')
            if news_author:
                print(news_author)
                f.write(news_author)
            else:
                news_author = ""
                f.write(news_author)
            print("7777777777777")
            f.write("," + news_name.replace('""', '/') + "," + news_story.replace(",", "/") + ","
                    + published_date + "," + "\n")
        print("6")
    else:
        print("nothing")


def web_crawler(max_pages):
    for i in range(0, 100):
        proxy_index = random_proxy()
        proxy = proxies[proxy_index]
        while True:
            try:
                print("1")
                count = 0
                req = Request('http://icanhazip.com')
                req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
                while count <= max_pages:
                    d = datetime.today() - timedelta(days=count)
                    d = d.strftime("%Y/%m/%d")
                    my_url = 'https://www.zakon.kz/' + str(d)
                    proxy_index = random_proxy()
                    proxy = proxies[proxy_index]
                    print(proxy)
                    print("22")
                    try:
                        my_ip = ureq(req).read().decode('utf8')
                        print(my_ip)
                    except:
                        del proxies[proxy_index]
                        print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
                        proxy_index = random_proxy()
                        proxy = proxies[proxy_index]
                    try:
                        print("2")
                        client = ureq(my_url, timeout=10.0)
                    except TimeoutError as time:
                        print(time)
                    except URLError as err:
                        print(err)
                    page_html = client.read()
                    client.close()
                    page_soup = soup(page_html, "html.parser")
                    containers = page_soup.findAll("div", {"class": "cat_news_item"})
                    print("3")

                    for container in containers:
                        comment_s = container.find_all("span", {"class": "comm_num"})
                        if comment_s:
                            comm_num = comment_s[0].text
                            print("4")
                            f.write(comm_num)
                        else:
                            space = ""
                            f.write(space)
                        for url_link in container.find_all('a', href=True):
                            href = 'https://www.zakon.kz' + url_link['href']
                            get_single_item(href)
                    count += 1
            except HTTPError as http:
                print("can't find given url", http)
            finally:
                print("Done crawling")
                return False


def random_proxy():
    return random.randint(0, len(proxies) - 1)


web_crawler(0)
f.close()
