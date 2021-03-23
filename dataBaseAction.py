import sqlite3

#  To Do
#  Add colomn in data.db 
#  Create founction startShift, stopShift


class dataBaseActions:

    def __init__(self):
        try:
            self.dataBase = sqlite3.connect('data.db')
            print("Succefuly connected to the database")
        except:
            print("Failed to connect to the database")
        self.cur = self.dataBase.cursor()
    
    def startShift(self, deliveryMan, startTime, startDate):
        pass

    def addDeliveryMan(self, name):
        command = """INSERT INTO livreurs (nomLivreur)  VALUES ("{}");""".format(name)
        self.cur.execute(command)
        self.dataBase.commit()

    def delDeliveryMan(self, name):
        command = """DELETE FROM livreurs WHERE nomLivreur="{}" """.format(name)
        self.cur.execute(command)
        self.dataBase.commit()

a = dataBaseActions()
a.delDeliveryMan("Alban")


    
     