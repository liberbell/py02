import requests
import xml.sax

class MycontentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slidecount = 0
        self.itemcount = 0

    def startDocument(self):
        print('About to start!')

    def endDocument(self):
        print('Finishing up!')

def main():
    handler = MycontentHandler()

    url = 'https://httpbin.org/xml'
    result = requests.get(url)
    print(result.text)

    print('There were {0} slides elements.'.format(handler.slidecount))
    print('There were {0} item elements.'.format(handler.itemcount))

if __name__ == '__main__':
    main()
