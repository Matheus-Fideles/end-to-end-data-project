from abc import ABC, abstractmethod

class RespiratoryDiseaseReader(ABC):

    @abstractmethod
    def read(self):
        pass