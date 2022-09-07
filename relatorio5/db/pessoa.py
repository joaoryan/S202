from db.database import Database


class Pessoa:
    def __int__(self):
        self.db = Database(database="cidade", collection="livros")
        self.collection = self.db.collection

    def create(self, titulo: str, autor: str, ano: int, preco: int):
        return self.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})

    def read(self):
        return self.collection.find({})

    def update(self, id: int, titulo: str, autor: str, ano: int, preco: int):
        return self.collection.update_one(
            {"_id": id},
            {
                "$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, id: int):
        return self.collection.delete_one({"_id": id})
