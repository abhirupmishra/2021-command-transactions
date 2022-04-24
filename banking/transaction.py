from abc import ABC


class Transaction(ABC):
    """
    Abstract transaction class
    """

    def execute(self) -> None:
        raise NotImplementedError()
    
    def undo(self) -> None:
        raise NotImplementedError()
    
    def redo(self) -> None:
        raise NotImplementedError()