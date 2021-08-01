import datetime
import datetime as dt


def get_today_cash_remained(currency):
    total_today = cash_calculator.get_today_stats()
    if total_today == 0:
        print("Денег нет, держись")
    else:
        if currency == 'usd':
            if total_today < 0:
                print(f"Денег нет, держись: твой долг - {round(total_today / cash_calculator.USD_RATE, 2), currency}")
            else:
                print(f"На сегодня осталось {round(total_today / cash_calculator.USD_RATE, 2)} {currency}")
        elif currency == 'eur':
            if total_today < 0:
                print(f"Денег нет, держись: твой долг - {round(total_today / cash_calculator.EUR_RATE, 2), currency}")
            else:
                print(f"На сегодня осталось {round(total_today / cash_calculator.EUR_RATE, 2)} {currency}")
        else:
            if total_today < 0:
                print(f"Денег нет, держись: твой долг - {total_today, currency}")
            else:
                print(f"На сегодня осталось {total_today} {currency}")


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):  # Добавить запись в список(records)
        self.records.append(record)

    def get_today_stats(self):  # Метод, который считает, сколько денег осталось на сегодня
        total_today = cash_calculator.limit
        for i in self.records:
            if i.date == dt.datetime.now().date():
                total_today -= i.amount
        return total_today

    def get_week_stats(self):
        week_stats = 0
        week_range = datetime.date.today() - datetime.timedelta(7)
        for i in self.records:
            if i.date >= week_range:
                week_stats += i.amount
        return week_stats


class Record:
    def __init__(self, amount, comment, date=None):
        self.date = date
        if self.date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()
        self.amount = amount
        self.comment = comment


class CashCalculator(Calculator):
    def __init__(self, limit):
        super(CashCalculator, self).__init__(limit)
        self.USD_RATE = 73.75
        self.EUR_RATE = 87.11


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="21.07.2021"))

get_today_cash_remained("eur")
# должно напечататься
# На сегодня осталось 555 руб

print(f"{cash_calculator.get_week_stats()} руб")

