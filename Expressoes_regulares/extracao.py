from urllib.request import urlopen
import json
import re

xml = urlopen("https://veja.abril.com.br/economia/").read()

xml_bruto = re.compile(r'<h2 class=\"title \">(.*?)<\/h2>')
lista_titulos = re.findall(xml_bruto,xml.decode("utf-8"))


with open('noticias_economia_VEJA.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(lista_titulos, indent=4)
    jp.write(js)
    

