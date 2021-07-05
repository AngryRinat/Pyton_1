from requests import get,utils
from datetime import datetime
from decimal import Decimal
import sys


def currency_rates(inp_arg):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    list_content = content.split('CharCode')
    dict = {}
    for i in range(1, len(list_content),2):
        course = list_content[i+1].split('Value')
        course[1] = course[1][1:-2]
        rate = Decimal(course[1].replace(',', '.'))
        dict[list_content[i][1:-2]] = rate.quantize((Decimal("1.00")))


    date_cur = datetime.today().strftime("%A %d %B %Y")
    course_cur = dict[inp_arg.upper()]
    return f"Today is {date_cur}, rate {inp_arg} to RUR is {course_cur}"




if __name__ == '__main__':
   print(currency_rates('USD'))

