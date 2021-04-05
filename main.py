from bs4 import BeautifulSoup as bs

import requests
import re



url = "https://keithgalli.github.io/web-scraping/example.html"
r = requests.get(url)

# Convertir a un objeto de beautiful soup

#soup = bs(r.content)
soup = bs(r.content, 'lxml')

#print(soup.prettify())

# find and find_all

first_header = soup.find("h2")
#print(f' first_header {first_header}' )

headers = soup.find_all("h2")
#print(f' headers {headers}')


# Pasar una lista de elementos

first_header = soup.find(["h1", "h2"])

headers = soup.find_all(["h1", "h2"])

#print(f' first_header {first_header}' )
#print(f' headers {headers}')


# Podemos pasarale atributos a find/find_all

paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
#print(paragraph)



# Podemos anidar llamadas

body = soup.find('body')
div = body.find('div')
header = div.find('h1')
#print(header)




# Podemos buscar una cadena específica en find/find_all

paragraphs = soup.find_all("p", string=re.compile("Some"))
#print(paragraph)

headers = soup.find_all("h2", string=re.compile("(H|h)eader"))
#print(header)

#select (CSS selector)

#print(soup.body.prettify())


content = soup.select("div p")
#print(content)

paragraphs = soup.select("h2 ~ p")
bold_text = soup.select("p#paragraph-id b")


paragraphs = soup.select("body > p")


for paragraph in paragraphs:
  paragraph.select("i")



#Obtener diferentes propiedades del HTML

header = soup.find("h2")
print(header.string)


div = soup.find("div")
print(div.prettify())
print(div.get_text())



link = soup.find("a")
print(link['href'])

paragraphs = soup.select("p#paragraph-id")
print(paragraphs[0]['id'])