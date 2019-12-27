# .py file for scraping Monet's landscapes
# Thomas patton (c) 2019
# Huge thanks to Robbie Barrat for inspiration

import time
import random
import requests
import bs4
from bs4 import BeautifulSoup
import urllib
import urllib.request
from urllib.parse import urljoin
import time


# Get all images on the page
def get_image_links(page):
    page_urls = []
    url = 'https://www.wikiart.org/en/claude-monet/by-Genre/landscape?json=1&layout=new&page=%d&resultType=masonry' % page
    resp = requests.get(url).json()
    for json_element in resp:
        page_urls.append(json_element["image"])
    return page_urls


def download_link(link, count):
    try:
        savepath = "../images/train/" + str(count) + ".jpg"
        time.sleep(0.2)  # try not to get a 403
        urllib.request.urlretrieve(link, savepath)
    except Exception as e:
        print("Failed to gather: " + str(link))


def main():
    image_urls = []
    for i in range(20):
        image_urls += get_image_links(i)

    j = 0
    for url in image_urls:
        print(url)
        print(j)
        download_link(url, j)
        j += 1

    print("FINISHED")




if __name__ == '__main__':
    main()
