class SqlQueries:

    @staticmethod
    def insertCar(model, modelYear, image, specifications, cost):
        return ("INSERT INTO cars"
                "(model, modelYear, image, specifications, cost)"
                "VALUES (%(model)s, %(modelYear)s, %(image)s, %(specifications)s, %(cost)s)")

    @staticmethod
    def deleteCar(model, modelYear, image, specifications, cost):
        return ("DELETE FROM cars "
                "WHERE (model=%(model)s AND modelYear=%(modelYear)s AND image=%(image)s AND specifications=%(specifications)s AND cost=%(cost)s)"
                "LIMIT 1")

    @staticmethod
    def selectAllCars():
        return "SELECT * FROM AutoService.cars"
