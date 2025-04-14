from abc import ABC, abstractmethod

class RespiratoryDiseaseReader(ABC):

    @abstractmethod
    def read(self, folder_path):
        pass