import requests

def main():
    url = 'https://httpbin.org/xml'
    result = requests.get(url)
    # printResult(result)

    url = 'https://httpbin.org/post'
    dataValues = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    result = requests.post(url, data=dataValues)
    # printResult(result)

    url = 'https://httpbin.org/get'
    headerValues = {
        "User-Agent": "Neo Tokyo App / 1.0.0"
    }
    result = requests.get(url, headers=headerValues)
    printResult(result)

def printResult(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Headers ------------')
    print(resData.headers)
    print('\n')

    print('Returned data ------')
    print(resData.text)

if __name__ == '__main__':
    main()
