
from requests import get,utils
from decimal import *


def currency_rates(inp_arg):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    list_content = content.split('CharCode')
    dict = {}
    for i in range(1, len(list_content),2):
        course = list_content[i+1].split('Value')
        course[1] = course[1][1:-2]
        dict[list_content[i][1:-2]] = course[1]

    return dict[str(inp_arg)]

print(currency_rates('GBP'))

