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


# Pull the JSON data corresponding to the page needed
def get_image_links(page):
    page_urls = []
    url = 'https://www.wikiart.org/en/claude-monet/by-Genre/landscape?json=1&layout=new&page=%d&resultType=masonry' % page
    resp = requests.get(url).json()
    for json_element in resp:
        page_urls.append(json_element["image"])
    return page_urls


# Download the image at the specified link
def download_link(link, count):
    try:
        savepath = "../images/train/" + str(count) + ".jpg"
        time.sleep(0.2)
        urllib.request.urlretrieve(link, savepath)
    except Exception as e:
        print("Failed to gather: " + str(link))


def main():
    image_urls = []     # Store all urls that need to be downloaded
    for i in range(20):
        image_urls += get_image_links(i)
    count = 0
    for url in image_urls:
        # print(url)
        print("Gathering image %d out of %d" % (count, len(image_urls)))
        download_link(url, count)
        count += 1

    print("FINISHED")




if __name__ == '__main__':
    main()
