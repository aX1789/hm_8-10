#Ми ця програма продажу, до нас має прийти клієнт, який хоче орендрувати машину, щоб ми це не забули в нас є система яка
# яка всі необхідні дані записує і щоб клієнт нам довіряв і все було чесно ми йому видаємо договір підтвердження
# Клієнт потребує змогу глянути які машини в нас є та звичайно що орендувати її, машина завжди має марку, модель та ще клієнт захоче
# бачити чи машина ціла чи машина з подряпинами. Система в свою чергу реєструє процес на ім'я клієнта, а також модель і марку записує
# далі він отримує договір


class Client:
    def __init__(self, name):
        self.name = name
    def check_available_cars():
        pass
    def rent_a_car(auto):
        pass
class Auto:
    def __init__(self, mark, model, state):
        self.mark = mark
        self.model = model
        self.state = state
    def is_rented():
        pass

class System:
    def take_a_request(name, car):
        pass

class Confirmation:
    def yourpass():
        pass

oursystem = System()


car1 = Auto("Audi", "A6", "have some scratches")


Max = Client("Max")
Max.check_available_cars()
Max.rent_a_car(car1)
oursystem.take_a_request(Max.name, car1)
confirm = Confirmation()
confirm.yourpass()


