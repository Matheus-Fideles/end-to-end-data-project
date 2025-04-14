from abc import ABC, abstractmethod

class RespiratoryDiseaseReader(ABC):

    @abstractmethod
    def read(self, topic_name):
        pass