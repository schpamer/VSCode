from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.htmlhttps://www.martindale.com/search/law-firms/?term=Insurance%20defense')
tree = html.fromstring(page.content)p
