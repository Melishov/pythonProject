class User:
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    def describe_user(self):
        print(f"Имя:{self.first_name}\nФамилия:"
              f"{self.last_name}\nВозраст:{self.age}\n"
              f"Профессия:{self.job}")

    def greet_user(self):
        print(f"Приветствуем Вас, {self.last_name} {self.first_name}!")


ilya=User("Илья", "Мелишов", "34", "Продавец")
ilya.describe_user()
ilya.greet_user()
