# reference https://docs.python.org/3/library/abc.html

from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(file):
        raise NotImplementedError
