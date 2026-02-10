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

df_cars = pd.read_csv("cars.csv", dtype={"id": str})
df_musik = pd.read_csv("musik.csv", dtype={"id": str})

class Auto:
    def __init__(self, id):
        self.id = id
        self.mark = df_cars.loc[df_cars["id"] == self.id, "make"].squeeze()
        self.model = df_cars.loc[df_cars["id"] == self.id, "model"].squeeze()
        self.year = df_cars.loc[df_cars["id"] == self.id, "year"].squeeze()
        self.state = df_cars.loc[df_cars["id"] == self.id, "state"].squeeze()
    def is_available(self):
        if self.id not in df_cars["id"].values:
            print(f"Помилка: Авто з ID {self.id} не знайдено в базі.")
            return False
        else:
            available = df_cars.loc[df_cars["id"] == self.id, "available"].squeeze()
            if available == "yes":
                return True
            else: 
                return False    
    
    def to_be_rented(self):
        df_cars.loc[df_cars["id"] == self.id, "available"] = "no"
        df_cars.to_csv("cars.csv", index=False)

class System:
    def __init__(self):
        pass
    def take_a_request(self, name, car):
        pass

class Confirmation:
    def __init__(self, cus_name, car, musik=None):
        self.cus_name = cus_name
        self.car = car
        self.musik = musik
    def yourpass(self):
        if self.musik:
            musik_information = f"""Musik Type: {self.musik.musiktype},
            Name of the playlisst: {self.musik.nameofplaylist},
            Link: {self.musik.link}"""
        else:
            musik_information = """
            You have chosen to drive without musik"""
        yourpass = f"""
        Thank you for your reservation
        Here is your booking data:
        Name: {self.cus_name}
        Car made: {self.car.mark}
        Car model: {self.car.model}
        Car year: {self.car.year}
        Car state: {self.car.state}
        {musik_information}"""
        return yourpass

class PlaylistServise:
    def __init__(self, id):
        self.id = id
        self.musiktype = df_musik.loc[df_musik["id"] == self.id, "Musik type"].squeeze()
        self.nameofplaylist = df_musik.loc[df_musik["id"] == self.id, "Name of playlist"].squeeze()
        self.link = df_musik.loc[df_musik["id"] == self.id, "Link"].squeeze()
def checking():

    print(df_cars)

    car_id = input("Enter the ID of the car: ")
    car = Auto(id=car_id)

    if car.is_available():
        car.to_be_rented()
        cus_name = input("Enter your name: ")
        music_suggestiong = input("Would you like some musik? Yes/No: ")
        if music_suggestiong == "Yes":
            print(df_musik)
            choice = input("Choose ID of the playlist: ")
            musik_choice = PlaylistServise(choice)
            your_pass = Confirmation(
            cus_name=cus_name,
            car = car,
            musik = musik_choice)
            print(your_pass.yourpass())
        else:    
            print("Whatever")
            your_pass = Confirmation(
                cus_name=cus_name,
                car=car,
            )
            print(your_pass.yourpass())
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

