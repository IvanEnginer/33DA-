class Meal:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return ': '.join([self.title, str(self.price)])

    def __repr__(self):
        """Функция, которая используется для текстового представления объекта в случаях, когда это происходит не
        через функцию str(obj)"""
        return str(self)

    def __add__(self, other):
        """Функция, которая описывает прибавление к нашему объекту объекта other"""
        # если у нас оба объекта данного класса, сложим их атрибуты
        if isinstance(other, Meal):
            new_title = ', '.join([self.title, other.title])
            new_price = self.price + other.price
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new_title = self.title + " и что-то еще"
            new_price = self.price + float(other)
        return Meal(new_title, new_price)

    __radd__ = __add__

    def __call__(self):
        self.title = "Ты всё съел!"
        self.price = -self.price
        print(self)
