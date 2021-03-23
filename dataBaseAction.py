import sqlite3

class dataBaseActions:

    def __init__(self):
        self.dataBase = sqlite3.connect('data.db')
        self.cur = self.dataBase.cursor()
    
    def startShift(self, deliveryMan, startTime, startDate):
        pass


dataBaseActions()

    
    