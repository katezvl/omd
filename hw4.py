import json
from keyword import iskeyword


class BaseAdvert:

    def __init__(self, ads):
        self.add_qualities(ads)

    def add_qualities(self, ads):
        for key, value in ads.items():
            if iskeyword(key):
                key = key + '_'
            setattr(self, key, value)
            if isinstance(value, dict):
                setattr(self, key, BaseAdvert(value))

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColourMixin:
    repr_color_code = 33

    def __repr__(self):
        text = super().__repr__()
        return f'\033[1;{self.repr_color_code};40m {text}'


class Advert(ColourMixin, BaseAdvert):
    def __init__(self, ads, *args, **kwargs):
        self._price = None
        if 'title' not in ads:
            raise ValueError('title is required')
        super().__init__(ads, *args, **kwargs)

    @property
    def price(self):
        return self._price or 0

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('must be >=0')
        self._price = value


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
    corgi_ad.price = 100
    print(corgi_ad)
