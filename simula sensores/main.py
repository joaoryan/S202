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

result = sensores.find({})

for c in result:
     pprint.pprint('--------------------')
     pprint.pprint(c)


def sensor1():
    while True:
        temp = random.randint(30, 40)
        print('Temperatura sensor 1: ', temp)
        sensores.update_one(
            {"nomeSensor": "Temp1"},
            {"$set": {"valorSensor": temp}}
        )
        if temp > 38:
            sensores.update_one(
                {"nomeSensor": "Temp1"},
                {"$set": {"sensorAlarmado": "true"}}
            )
            print('Atenção! Temperatura muito alta! Verificar Sensor Temp1!')
            break

        time.sleep(2)


x = threading.Thread(target=sensor1)
x.start()


def sensor2():
    while True:
        temp = random.randint(30, 40)
        print('Temperatura sensor 2: ', temp)
        sensores.update_one(
            {"nomeSensor": "Temp2"},
            {"$set": {"valorSensor": temp}}
        )
        if temp > 38:
            sensores.update_one(
                {"nomeSensor": "Temp2"},
                {"$set": {"sensorAlarmado": "true"}}
            )
            print('Atenção! Temperatura muito alta! Verificar Sensor Temp2!')
            break

        time.sleep(3)


x = threading.Thread(target=sensor2)
x.start()


def sensor3():
    while True:
        temp = random.randint(30, 40)
        print('Temperatura sensor 3: ', temp)
        sensores.update_one(
            {"nomeSensor": "Temp3"},
            {"$set": {"valorSensor": temp}}
        )
        if temp > 38:
            sensores.update_one(
                {"nomeSensor": "Temp3"},
                {"$set": {"sensorAlarmado": "true"}}
            )
            print('Atenção! Temperatura muito alta! Verificar Sensor Temp3!')
            break

        time.sleep(4)

x = threading.Thread(target=sensor3)
x.start()
