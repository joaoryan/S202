import pprint

from pymongo import MongoClient

# variavel que recebe conexao com mongoDB
client = MongoClient('mongodb://localhost:27017')

# variavel que recebe uma conexao com database
db = client['dbworld']

# variavel que recebe uma conexao com uma Collection
countries = db.countries

# variavel que recebe os documentos
result = countries.find(
    {'capital': 'Brasília'},
    {'name.common': 1, '_id': 0}
)

for c in result:
    pprint.pprint(c)
