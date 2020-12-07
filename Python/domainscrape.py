import re

def domain_name(url):
    return print(re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name'))

domain_name('"http://www.zombie-bites.com"')

# import tldextract
 
# list = tldextract.extract('https://www.cnet.com')
 
# domain_name = list.domain

# print(domain_name)