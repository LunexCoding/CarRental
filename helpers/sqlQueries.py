class SqlQueries:

    @staticmethod
    def insertCar(model, year, image, specifications, cost):
        return ("INSERT INTO cars"
                "(model, year, image, specifications, cost)"
                "VALUES (%(model)s, %(year)s, %(image)s, %(specifications)s, %(cost)s)")

    @staticmethod
    def deleteCar(model, year, image, specifications, cost):
        return ("DELETE FROM cars "
                "WHERE model=%(model)s AND year=%(year)s AND image=%(image)s AND specifications=%(specifications)s AND cost=%(cost)s")

    @staticmethod
    def selectAllCars():
        return "SELECT * FROM AutoService.cars"