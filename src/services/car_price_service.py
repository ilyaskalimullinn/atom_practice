import math
from datetime import date

from db.models import Car, CarUsage


class CarPriceService:

    def calc_car_price(self, car: Car) -> int:
        # some crazy logic here :)
        # could as well just add some ML algorithm

        coeff = 1

        coeff *= self.calc_manufacture_date_coefficient(car.manufacture_date)
        coeff *= self.calc_mileage_coefficient(car.mileage)
        coeff *= self.calc_usage_coefficient(car.usage)
        coeff *= self.calc_plate_number_coefficient(car.plate_number)

        return math.floor(coeff * car.model.base_price)

    def calc_manufacture_date_coefficient(self, manufacture_date: date) -> float:
        diff = date.today() - manufacture_date
        return min(1 - 1 / math.log(diff.days / 365, 3), 1)

    def calc_mileage_coefficient(self, mileage: int) -> float:
        return 1 - mileage / 500000

    def calc_usage_coefficient(self, usage: CarUsage) -> float:
        if usage is None:
            return 1
        else:
            return 1.2

    def calc_plate_number_coefficient(self, plate_number: str) -> float:
        return math.log2(1 + 2 * len(set(plate_number)) / len(plate_number))
