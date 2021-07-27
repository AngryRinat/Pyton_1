import re


def email_parse(inp_str):
    POST_DOMAIN = re.compile(r'@(\w+[.]\w+)')

    USER_NAME = re.compile(r'(^\w+)@')

    if len(re.findall(POST_DOMAIN, inp_str)) == 0 or len(re.findall(USER_NAME, inp_str)) == 0:
        raise ValueError(f'Wrong email: {inp_str}')

    print(f'username: {re.findall(USER_NAME, inp_str)}, domain: {re.findall(POST_DOMAIN, inp_str)}')


email_parse('kateg@list.ru')
