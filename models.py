from typing import List

from pydantic import BaseModel, Field


class IntervalsModel(BaseModel):
    lesson: List[int] = Field(..., min_items=2, max_items=2)
    pupil: List[int] = Field(..., min_items=2)
    tutor: List[int] = Field(..., min_items=2)
