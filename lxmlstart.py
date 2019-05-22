import requests
from lxml import etree

def main():
    url = 'https://httpbin.org/xml'
    result= requests.get(url)

    doc = etree.fromstring(result.content)
    print(result.text)

    print(doc.tag)
    print(doc.attrib['title'])

    for elem in doc.findall('slide'):
        print(elem.tag)

    newSlide = etree.SubElement(doc, 'slide')
    newSlide.text = 'This is a new slide'

    slidecount = len(doc.findall('slide'))
    itemcount = len(doc.findall('.//item'))

    print('There are {0} slide elements.'.format(slidecount))
    print('There are {0} item elements.'.format(itemcount))


if __name__ == '__main__':
    main()
