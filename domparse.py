import xml.dom.minidom
import requests

def main():
    url = 'https://httpbin.org/xml'
    result = requests.get(url)


if __name__ == '__main__':
    main()
