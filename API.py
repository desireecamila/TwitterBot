#Camila Osoria
#801155816
#Prof Carlos Corrada
#Twitter API

#https://apps.twitter.com/app/12493377/keys
#https://pypi.python.org/pypi/twitter/1.17.1#downloads
#https://github.com/basti2342/retweet-bot/blob/master/retweet.py
#https://dev.twitter.com/rest/public/search

#username: tripleta intelectual
#password: desiree

from twitter import *
import json

#Se conecta al API de Twitter
t = Twitter(
            auth=OAuth('743154858824343552-DBPRpivcsDQIMIW6mwvPakokJI2KAeG',
                       '8K52cI0lQohQ5lyNfceQORTthp3dNmZcoPIbZwW70jk98',
                       'gRkgYqfCbsnNE2tN80b8GYrii',
                       '5waAx0ZOuw5sjEJrhFSwmDvIHDNER2T9N8uUBa7KKr1x0Ertvx'))


#Tweet del trabajo escrito
#t.statuses.update(status="Poner el trabajo escrito aqui")

#lo que se buscara
pregunta = "#Bacalao"

#Busqueda de tweets relacionados
respuesta = t.search.tweets(q=pregunta, count = 2) #count es el numero de tweets que cogera

#Itera por los tweets

for tweets in respuesta["statuses"]:
    #print tweets
    parsed_json = json.loads(tweets)
    

#for tweets in respuesta["statuses"]:

    
    #t.statuses.retweet(id = tweets['id']) #aqui se hace el retweet
    #print "Hicistes retweet de" + str(tweets['id'])
    #t.friendships.create(user_id=tweets['user']['id']) #aqui se hace el follow a la persona
    #print "Te hicistes amigo de" + str(tweets['user']['id'])    
