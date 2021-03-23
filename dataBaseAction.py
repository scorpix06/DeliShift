import sqlite3

class dataBaseActions:

    def __init__(self):
        self.dataBase = sqlite3.connect('shift.db')
        self.cur = dataBase.cursor()
    
    def startShift(self, deliveryMan, startTime, startDate):
        pass

    
    