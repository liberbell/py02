import requests
from lxml import etree

def main():
    url = 'https://httpbin.org/xml'
    resutl = requests.get(url)

    doc = etree.fromstrint(result.content)
    print(result.text)


if __name__ == '__main__':
    main()
