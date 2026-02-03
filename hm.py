#Ми ця програма продажу, до нас має прийти клієнт, який хоче орендрувати машину, щоб ми це не забули в нас є система яка
# яка всі необхідні дані записує і щоб клієнт нам довіряв і все було чесно ми йому видаємо договір підтвердження
# Клієнт потребує змогу глянути які машини в нас є та звичайно що орендувати її, машина завжди має марку, модель та ще клієнт захоче
# бачити чи машина ціла чи машина з подряпинами. Система в свою чергу реєструє процес на ім'я клієнта, а також модель і марку записує
# далі він отримує договір


# class Client:
#     def __init__(self, name):
#         self.name = name
#     def check_available_cars(self):
#         pass
#     def rent_a_car(self, auto):
#         pass

import pandas as pd

class Auto:
    def __init__(self, id, make, model, state):
        self.id = id
        self.mark = make
        self.model = model
        self.state = state
    def is_available(self):
        pass
    def to_be_rented(self):
        pass

class System:
    def __init__(self):
        pass
    def take_a_request(self, name, car):
        pass

class Confirmation:
    def __init__(self, cus_name, car):
        self.cus_name = cus_name
        self.car_num = car
    def yourpass(self):
        pass

def checking():
    df = pd.read_csv("cars.csv")
    print(df)

    car_id = input("Enter the ID of the car")
    car = Auto(id=car_id)

    if car.is_available():
        car.to_be_rented()
        cus_name = input("Enter your name: ")
        your_pass = Confirmation(
            cus_name=cus_name,
            car = car
        )
        Confirmation.yourpass()
    else: 
        print("this car is not in your reach")

if __name__ == "__main__":
    # добавив щоб добавить
    checking()

# oursystem = System()
# car1 = Auto("Audi", "A6", "have some scratches")
# Max = Client("Max")
# Max.check_available_cars()
# Max.rent_a_car(car1)
# oursystem.take_a_request(Max.name, car1)
# confirm = Confirmation()
# confirm.yourpass()

