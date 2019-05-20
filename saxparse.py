import requests
import xml.sax

class MycontentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slidecount = 0
        self.itemcount = 0

def main():
