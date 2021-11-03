class points2Function(object):
    __slope: float
    __intercept: float

    def setPoints (self, x1: float, y1: float, x2: float, y2: float):
        self.__calculateSlope(x1, y1, x2, y2)
        self.__calculateIntercept(x1, y1)

    def __init__(self, *args):
        for item in args:
            if type(item) is not float:
                raise RuntimeError("Argumentos de tipos incompatíveis.")
        if len(args) == 4:
            self.setPoints(args[0], args[1], args[2], args[3])
        elif len(args) != 0:
            raise RuntimeError("Quantidade errada de argumentos.")

    def __calculateSlope(self, x1: float, y1: float, x2: float, y2: float):
        self.__slope = (y2 - y1)/(x2-x1)
    def __calculateIntercept(self, x: float, y: float):
        self.__intercept = (-1* self.__slope * x) + y

    def function(self, x: float):
        return (self.__slope * x) + self.__intercept
    def inverse(self, y: float):
        return (y - self.__intercept)/self.__slope
