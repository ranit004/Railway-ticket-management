from random import randint

class train():
    def __init__(self, trainNo) -> None:
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket has been booked in trainNo is : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is runnig on time")

    def getFare(self, fro , to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(444,6789)}")

a = train(randint(345, 4560))
a.book("Kalyani" , "Kolkata")
a.getStatus()
a.getFare("Kalyani", "Kolkata")