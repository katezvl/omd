import json


class BaseAdvert:
    price = 0
    repr_color_code = 33

    def __init__(self):
        pass

    def adder(self, ads):
        for key, value in ads.items():
            setattr(self, key, value)
            if key == 'location':
                for a, b in ads['location'].items():
                    setattr(self, a, b)
            if self.price < 0:
                raise ValueError('must be >= 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColourMixin:

    def __repr__(self):
        text = super().__repr__()
        return f'\033[1;{super().repr_color_code};40m {text}'


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
    lesson_ad = Advert()
    lesson_ad.adder(lesson)
    print(lesson_ad.price)
    corgi = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }
    corgi_ad = Advert()
    corgi_ad.adder(corgi)

