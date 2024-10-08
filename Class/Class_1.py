class Restaraunt:
    def __init__(self,restaraunt_name,cuisine_type):
        self.name=restaraunt_name
        self.type=cuisine_type
    def describe_restaurant(self):
        print(f"Тип ресторана: {self.name}\nНазвание ресторана: {self.type}")
    def open_restaraunt(self):
        print("Ресторан открыт!")
amato=Restaraunt("Амато","Японский")
print(amato.name)
print(amato.type)
amato.describe_restaurant()
amato.open_restaraunt()