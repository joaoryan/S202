from bson import ObjectId

from db.database import Database

class AulaDB:
    def __init__(self):
        self.db = Database(database="atlas-cluster", collection="Aulas")
        #self.db.resetDatabase()
        self.collection = self.db.collection

    def getAllAulas(self):
        response = self.collection.find({})
        aulas = []
        for aula in response:
            aulas.append(aula)
        return aulas

    def createAula(self,submitAula):
        return self.collection.insert_one(submitAula)


    def updateAula(self, id, submitEdit):
        return self.collection.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": submitEdit,
                "$currentDate": {"lastModified": True}
            }
        )

    def deleteAula(self, _id):
        return self.collection.delete_one({"_id":  ObjectId(_id)})
