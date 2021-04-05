# BeautifulSoup-Course

1. [Enlaces ](#schema20)

<hr>

<a name="schema1"></a>

# 1. Instalar librerias necesarias
~~~python
conda install -c anaconda beautifulsoup4
conda install -c anaconda lxml
~~~

<hr>

<a name="schema2"></a>

# 2. Importamos librerías 
~~~python
from bs4 import BeautifulSoup
~~~
<hr>

<a name="schema3"></a>

# 3. Cargamos el html

with open('nombre_archivo.html', 'modo:r = lectura') as nombre_archivo:
    guardar_contenido = nombre_archivo.read()

~~~python
with open ('home.html', 'r') as html_file:
    content = html_file.read()
    print(content)
~~~
![img](./images/001.png)

<hr>

<a name="schema4"></a>

# 4.  Creamos instancia soup
~~~python
soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())
~~~
![img](./images/001.png)

<hr>

<a name="schema5"></a>

# 5. Buscamos las etiquetas o tags h5
~~~python
tags = soup.find('h5')
print(tags)
~~~
Con `soup.find` solo obtenemos el primero
![img](./images/002.png)


Con `soup.find_all` los obtenemos.
~~~python
courses_html_tags = soup.find_all('h5')
print(courses_html_tags)
~~~
![img](./images/003.png)


Obtener solo el texto de las tags
~~~python
for course in courses_html_tags:
    print(course.text)
~~~

![img](./images/004.png)






http://www.jimshapedcoding.com/courses/Python%20Web%20Scraping


https://www.youtube.com/watch?v=XVv6mJpFOb0&t=34s