class Film:

    instance = None

    def __init__(self, title = None, director = None, year = None,marks=0,rating=0):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__marks = marks
        self.__rating = rating

    def __str__(self):
        return f"Video(title='{self.__title}', director='{self.__director}'" \
               f", year={self.__year}, marks={self.__marks}, rating={self.__rating})"

    def rate(self, mark):
        if mark > 10:
            mark = 10
        elif mark < 1:
            mark = 1
        self.rating = (self.__rating * self.__marks + mark) / (self.__marks + 1)
        self.__marks += 1

    def getCurrentRating(self):
        return self.__rating

    @staticmethod
    def getInstance(self):
        if Film.instance is None:
            Film.instance = Film()
        else:
            return Film.instance

films = [Film(),Film.getInstance()]
