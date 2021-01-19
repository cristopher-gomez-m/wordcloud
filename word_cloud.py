
from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

#Hacemos dos funciones,de acuerdo a la pagina a la que se vaya a hacer la petición
def busqueda_es():
    ID= input("Ingrese el id del usuario que desea hacer la imagen de nubes de palabras: ")
    
    page = requests.get('https://es.stackoverflow.com/users/{}/?tab=tags'.format(ID))   
    page2= requests.get('https://es.stackoverflow.com/users/{}/?tab=tags'.format(ID)) 
    return page,page2

def busqueda_en():
    ID= input("Ingrese el id del usuario que desea hacer la imagen de nubes de palabras: ")
    page = requests.get('https://stackoverflow.com/users/{}/?tab=tags'.format(ID))   
    page2= requests.get('https://stackoverflow.com/users/{}/?tab=tags'.format(ID)) 
    return page,page2

if __name__ == "__main__":
    idioma=input("Ingrese es si el ID es de stackoverflow español o en si el ID de stackoverflow ingles: ")
    if idioma == "en":
        page,page2=busqueda_en()
    
    
    elif idioma == "es":
        page,page2=busqueda_es()
    #Ya sea español o ingles,se utiliza el mismo nombre para reducir las lineas de código


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
    #Se comprime en un diccionario para darle una llave y un valor para pasarlo al wordcloud
    word_cloud = WordCloud(height=800, width=800, background_color='white',max_words=150, min_font_size=5).generate_from_frequencies(diccionario) 
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    #Se comprime en un plano 2d y se oculta el plano cartersiano
    plt.show()
    