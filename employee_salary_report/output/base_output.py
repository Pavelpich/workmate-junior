from abc import ABC, abstractmethod

class OutputFormatter(ABC):
    @abstractmethod
    def render(self, data: dict) -> str:
        raise NotImplementedError