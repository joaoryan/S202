import pprint
s
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
