class TV_show:
    """Класс сериалы. Содержит информацию о сериале: название, рейтинг, год выпуска"""
    # Переменная содержит количество сериалов в классе
    quantity = 0
    def __init__(self, name, rating, year, **kwargs) -> None:
        self.name = name
        self.rating = rating
        self.year = year 
        super().__init__(**kwargs)
        TV_show.quantity += 1
        
    def about_shows(self):
        print (f'Название {self.name}, рейтинг {self.rating}. Год выпуска {self.year}')

BrakingBad = TV_show("BB", "7.8","2000")
BrakingBad.about_shows()
print ("количество сериалов", TV_show.quantity)   
        
class Animations(TV_show):
    """Класс мультипликационных сериалов. Имеет информацию о стране производства"""
    def __init__(self, name, rating, year, country, **kwargs) -> None:
        super().__init__(name, rating, year, **kwargs)
        self.country = country

    def about_shows(self):
        print("Это мультипликационный сериал. ", end="")
        super().about_shows()
        print (f'Страна производства {self.country}')

RickMorti = Animations("rick", "9", "2020", "USA")
RickMorti.about_shows()
print ("количество сериалов", TV_show.quantity)  

class Comedy(TV_show):
    """Класс комедийных сериалов. Имеет информацию о количестве сезонов"""
    def __init__(self, name, rating, year, numb_seasons, **kwargs) -> None:
        super().__init__(name, rating, year, **kwargs)
        self.seasons = numb_seasons

    def about_shows(self):
        print("Это комедийный сериал. ", end="")
        super().about_shows()
        print (f'Количество сезонов {self.seasons}') 

Friends = Comedy("Friends", "9", "1995", "3")
Friends.about_shows()
print ("количество сериалов", TV_show.quantity)  

class Animation_Comedy(Comedy, Animations):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs) 
        


    def about_shows(self):
        print("Это мультипликационный комедийный сериал", f'Название {self.name}, рейтинг {self.rating}. Год выпуска {self.year}')
        print (f'Страна производства {self.country} ', end="")
        print (f'Количество сезонов {self.seasons}') 

Simsons = Animation_Comedy(name="Simsons", rating="8.8", year="2021", numb_seasons="14", country="USA")
Simsons.about_shows()
print ("количество сериалов", TV_show.quantity)
