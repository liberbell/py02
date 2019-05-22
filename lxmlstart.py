import requests
from lxml import etree

def main():
    url = 'https://httpbin.org/xml'
    resutl = requests.get(url)
