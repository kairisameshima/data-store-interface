from abc import ABC, abstractmethod


class DataStoreInterface(ABC):
    @abstractmethod
    def get(self, key: str) -> str:
        pass

    @abstractmethod
    def set(self, key: str, value: str) -> None:
        pass

    @abstractmethod
    def delete(self, key: str) -> None:
        pass

    @abstractmethod
    def begin(self) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass
    