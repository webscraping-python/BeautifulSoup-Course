from bs4 import BeautifulSoup

with open ('home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

# Creamos instancia soup
soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

# Buscamos las etiquetas o tags h5
tags = soup.find('h5')
#print(tags)
#con soup.find solo obtenemos el primero

courses_html_tags = soup.find_all('h5')
#print(courses_html_tags)

#Obtener solo el texto de las tags

for course in courses_html_tags:
    print(course.text)