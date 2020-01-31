class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def numbers(cls, date):
        num = list(map(int, date.split('-')))
        return num

    @staticmethod
    def check(date):
        data = Date.numbers(date)
        if 0 < data[0] <= 31:
            pass
        else:
            print('Ошибка в дне')
        if 0 < data[1] <= 12:
            pass
        else:
            print('Ошибка в месяце')
        if 0 < data[2] <= 2050:
            pass
        else:
            print('Ошибка в годе')


Date.check('1-1-1987')

data = Date('13-04-1987')
