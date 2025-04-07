from typing import Dict, List, Union, Optional
from pydantic import BaseModel

class Entity(BaseModel):
    id: Optional[int] = None
    addition: Dict[str, Union[str, int, Optional[int]]]
    important_numbers: List[int]
    title: str
    verified: bool