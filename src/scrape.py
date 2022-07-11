from bs4 import BeautifulSoup
import requests


def scrape(website_link, link_class):
    """
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: response = list; list of events
    """

    # get content of website and parse it
    website_request = requests.get(website_link, timeout=5)
    website_content = BeautifulSoup(website_request.content, 'html.parser')

    # extract job description
    response = website_content.find_all(class_=link_class)
    return response
