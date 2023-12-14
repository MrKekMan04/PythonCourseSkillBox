from abc import ABC


class CustomException(Exception, ABC):
    @staticmethod
    def get_cause() -> str:
        ...


class KillError(CustomException):
    @staticmethod
    def get_cause() -> str:
        return "Kill!"


class DrunkError(CustomException):
    @staticmethod
    def get_cause() -> str:
        return "Drunk!"


class CarCrashError(CustomException):
    @staticmethod
    def get_cause() -> str:
        return "Car crash!"


class GluttonyError(CustomException):
    @staticmethod
    def get_cause() -> str:
        return "Gluttony!"


class DepressionError(CustomException):
    @staticmethod
    def get_cause() -> str:
        return "Depression"
