import re

phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
no_search = phone_number.search('Number is 123-456-7890')
print('Number found: ' + no_search.group())
