class Client:
    def __init__(self, name, second_name,
                 city, balance):
        self.name = name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'\"{self.name} {self.second_name} {self.city} Баланс: {self.balance} руб.\"'

    def get_client(self):
        return f'{self.name} {self.second_name} {self.city}'


client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Василий', 'Иванов', 'Пенза', 100)
client_3 = Client('Егор', 'Сидоров', 'Самара', 200)
client_4 = Client('Алексей', 'Кузнецов', 'Вологда', 67)

client_list = [client_1.get_client(), client_2.get_client(), client_3.get_client(), client_4.get_client()]

print(client_1)

for client in client_list:
    print(client)
