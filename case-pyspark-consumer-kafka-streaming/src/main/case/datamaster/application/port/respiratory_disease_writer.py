from abc import ABC, abstractmethod

class RespiratoryDiseaseWriter(ABC):

    @abstractmethod
    def write(self, df):
        pass