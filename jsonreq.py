import json
import requests

def main():
    url = 'https://httpbin.org/json'
    result = requests.get(url)

    dataobj = result.json()
    print(json.dumps(dataobj, indent=4))

    print(list(dataobj.key))


if __name__ == '__main__':
    main()
