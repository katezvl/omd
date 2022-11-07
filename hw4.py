import json
from keyword import iskeyword


class BaseAdvert:
    repr_color_code = 33

    def __init__(self, ads):
        self.add_qualities(ads)

    def add_qualities(self, ads):
        if 'price' not in ads:
            ads['price'] = 0
        for key, value in ads.items():
            if iskeyword(key):
                key = key + '_'
            setattr(self, key, value)
            if isinstance(value, dict):
                setattr(self, 'location', BaseAdvert(ads['location']))
            if key == 'price' and value < 0:
                raise ValueError('must be >= 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('must be >=0')
        self._price = value


class ColourMixin:
    repr_color_code = 33

    def __repr__(self):
        text = super().__repr__()
        return f'\033[1;{self.repr_color_code};40m {text}'


class Advert(ColourMixin, BaseAdvert):
    pass


if __name__ == '__main__':
    lesson_str = """{
                  "title": "python",
                  "price": 3,
                  "location": {
                      "address": "город Москва, Лесная, 7",
                      "metro_stations": ["Белорусская"]
                      }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)
    corgi = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }
    corgi_ad = Advert(corgi)
    corgi_ad.price = -1
    print(corgi_ad.class_)
