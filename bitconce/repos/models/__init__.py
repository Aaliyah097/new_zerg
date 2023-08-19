from abc import abstractmethod, ABC
from datetime import datetime


class DataMixin(ABC):
    @abstractmethod
    def __init__(self, source: dict):
        for key, value in source.items():
            if key in self.__dict__:
                if value in ['None', None]:
                    continue

                key_type = type(self.__getattribute__(key))
                if key_type == datetime:
                    try:
                        value = datetime.strptime(value, "%d.%m.%y, %H:%M")
                    except ValueError:
                        try:
                            value = datetime.strptime(value, "%d.%m.%Y, %H:%M")
                        except ValueError:
                            value = datetime.now()
                elif key_type == int:
                    value = int(value)
                elif key_type == float:
                    value = float(value)
                elif key_type == str:
                    value = str(value)

                self.__setattr__(key, value)

    def __str__(self):
        return str(self.serialize())

    def serialize(self) -> dict:
        return self.__dict__
