
from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

if __name__ == "__main__":


    ID= input("Ingrese el id del usuario que desea hacer la imagen de nubes de palabras: ")
    page = requests.get('https://es.stackoverflow.com/users/{}/?tab=tags'.format(ID))   
    page2= requests.get('https://es.stackoverflow.com/users/{}/?tab=tags'.format(ID))
    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(page2.content, 'html.parser')

    palabras = soup.find_all('a', class_='post-tag')
    numeros = soup.find_all('span',class_='item-multiplier-count' )

    pb = list()

    num= list()
    for i in numeros:
        num.append(i.text)
     

 

    for j in palabras:
        pb.append(j.text)
        
    if pb[0] == pb[0]:
       pb.pop(0)
    #Se crea una lista para cada columna de estiquetas,se vaa a trabajar con 2 columnas
    nueva_lista = list()
    segunda_lista= list()

    #Se agrega los datos de la segunda colunma
    for key,value in enumerate(pb):
        if key%4 ==0:
            segunda_lista.append(pb[key+1])

    #Se agrega los datos de la primera columna a la primera lista
    for key,value in enumerate(pb):
        if key%4 ==0:
            nueva_lista.append(pb[key])
        
    nueva_lista += segunda_lista
    
    lista_numeros= [int(x) for x in num]

    list.sort(lista_numeros,reverse=True)
    


    diccionario= dict(zip(nueva_lista,lista_numeros))
    #Se comprime en un diccionario para darle una llave y un valor para pasarlo al wordcloud
    print(diccionario)
    
    

    word_cloud = WordCloud(height=300, width=500, background_color='white',max_words=20, min_font_size=5).generate_from_frequencies(diccionario) 
    #Se comprime en un plano 2d y se oculta el plano cartersiano
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    