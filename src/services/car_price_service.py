from db.models import Car


class CarPriceService:

    def calc_car_price(self, car: Car):
        return 1e6 / (car.mileage + 1)
