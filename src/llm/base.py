from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any,Union

class LLMBase(ABC):
    @abstractmethod
    def generate(self, prompt : str) ->str:
        pass