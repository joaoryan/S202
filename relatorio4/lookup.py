from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.pessoa_dataset import dataset as pessoa_dataset
from dataset.produto_database import dataset as produto_dataset

pessoas = Database(
    database="database",
    collection="pessoas",
    dataset=pessoa_dataset
)
pessoas.resetDatabase()

produto = Database(
    database="database",
    collection="produtos",
    dataset=produto_dataset
)
produto.resetDatabase()

result1 = produto.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",  # outra colecao
            "localField": "cliente_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "dono"  # nome da saida
        }
    },
    {"$group": {"_id": "$cliente_id", "total": {"$sum": "$total"}}},
    {"$sort": {"total": -1}},
    {"$unwind": '$_id'},
    {"$project": {
        "_id": 0,
        "nome": 1,
        "total": 1,
        "desconto": {
            "$cond": {"if": {"$gte": ["$total", 10]}, "then": 'true', "else": 'false'}
        }
    }}
])

writeAJson(result1, "result1")
