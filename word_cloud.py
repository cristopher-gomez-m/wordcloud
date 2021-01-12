
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt

ID= input("Ingrese el id del usuario que desea hacer la imagen de nubes de palabras: ")


page = requests.get('https://es.stackoverflow.com/users/{}/?tab=tags'.format(ID))  
page2= requests.get('https://es.stackoverflow.com/users/{}/?tab=tags'.format(ID))

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')

palabras = soup.find_all('a', class_='post-tag')
numeros = soup.find_all(class_='item-multiplier-count' )

pb = list()

num= list()

for i in numeros:
    num.append(i.text)


for j in palabras:
    pb.append(j.text)

lista_numeros= [int(x) for x in num]

diccionario= dict(zip(pb,lista_numeros))
print(diccionario)




word_cloud = WordCloud(height=800, width=800, background_color='white',max_words=150, min_font_size=5).generate_from_frequencies(diccionario) 
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()