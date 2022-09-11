import pprint
import random
import time
import threading

from pymongo import MongoClient

# variavel que recebe conexao com mongoDB
client = MongoClient('mongodb://localhost:27017')

# variavel que recebe uma conexao com database
db = client['bancoiot']

# variavel que recebe uma conexao com uma Collection
sensores = db.sensores

# variavel que recebe os documentos
result = sensores.find({})

for c in result:
    pprint.pprint('--------------------')
    pprint.pprint(c)


def sensor1():
    while True:
        temp = random.randint(30, 40)
        print('Temperatura sensor 1: ', temp)
        time.sleep(2)
        if temp > 38:
            print('Atenção! Temperatura muito alta! Verificar Sensor 1!')
            break


x = threading.Thread(target=sensor1)
x.start()


def sensor2():
    while True:
        temp = random.randint(30, 40)
        print('Temperatura sensor 2: ', temp)
        time.sleep(3)
        if temp > 38:
            print('Atenção! Temperatura muito alta! Verificar Sensor 2!')
            break


x = threading.Thread(target=sensor2)
x.start()


def sensor3():
    while True:
        temp = random.randint(30, 40)
        print('Temperatura sensor 3: ', temp)
        time.sleep(4)
        if temp > 38:
            print('Atenção! Temperatura muito alta! Verificar Sensor 3!')
            break


x = threading.Thread(target=sensor3, args=())
x.start()
