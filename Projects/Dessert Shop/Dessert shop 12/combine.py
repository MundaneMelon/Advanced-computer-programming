import typing
from abc import *
from desserts import *
from typing import *

@typing.runtime_checkable
class Combine(Protocol):

    @abstractmethod
    def can_combine(self, other: "Combinable") -> bool:
        pass

    @abstractmethod
    def combine(self, other: "Combinable") -> "Combinable":
        pass

