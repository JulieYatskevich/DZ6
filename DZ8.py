class TV_show:
    """Класс сериалы. Содержит информацию о сериале: название, рейтинг, год выпуска"""
    # Переменная содержит количество сериалов в классе
    quantity = 0
    
    def __init__(self, name, rating:float, year, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.rating = rating
        self.year = year 
        TV_show.quantity += 1
        
    def about_shows(self):
        print (f'Название {self.name}, рейтинг {self.rating}. Год выпуска {self.year}')

    @staticmethod
    def sum_TVshow():
        """Выводит количество сериалов в базе"""
        print(f'Количество сериалов в базе , {TV_show.quantity}')
    

class Animation(TV_show):
    """Класс мультипликационных сериалов. Имеет информацию о стране производства"""
    min_rating = 8

    @classmethod
    def popular(cls, rat):
        return cls.min_rating <= rat

    def __init__(self, name, rating:float, year, country, **kwargs) -> None:
        super().__init__(name, rating, year, **kwargs)
        self.country = country
        if self.popular(rating):
            print ("Популярный")
        else: 
            print ("Непопулярный")

    def about_shows(self):
        print("Это мультипликационный сериал. ", end="")
        super().about_shows()
        print (f'Страна производства {self.country}')






class Comedy(TV_show):
    """Класс комедийных сериалов. Имеет информацию о количестве сезонов"""
    def __init__(self, name, rating:float, year, numb_seasons, **kwargs) -> None:
        super().__init__(name, rating, year, **kwargs)
        self.seasons = numb_seasons

    def about_shows(self):
        print("Это комедийный сериал. ", end="")
        super().about_shows()
        print (f'Количество сезонов {self.seasons}') 



class Animation_Comedy(Comedy, Animation):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs) 
        


    def about_shows(self):
        print("Это мультипликационный комедийный сериал", f'Название {self.name}, рейтинг {self.rating}. Год выпуска {self.year}')
        print (f'Страна производства {self.country} ', end="")
        print (f'Количество сезонов {self.seasons}') 

    


breakingBad = TV_show("BreakingBad", 7.8,"2000")
breakingBad.about_shows()


rickMorti = Animation("rick", 9, "2020", "USA")
rickMorti.about_shows()

simsons = Animation_Comedy(name="Simsons", rating=7, year="2021", numb_seasons="14", country="USA")
simsons.about_shows()

friends = Comedy("Friends", 9, "1995", "3")
friends.about_shows()

print(TV_show.sum_TVshow())




