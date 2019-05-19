import json

def main():
    jsonStr = '''{
        "sandwich": "Reuben",
        "toasted": True,
        "toppings": [
            "Thousand Island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "price": 8.99
    }'''

    data = json.loads(jsonStr)

    print('Sandwich: ' + data['sandwich'])
    if (data['toasted']):
        print('And it`s toasted!')

if __name__ == '__main__':
    main()
