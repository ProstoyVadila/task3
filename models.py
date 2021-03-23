from pydantic import BaseModel, Field


class IntervalsModel(BaseModel):
    lesson: list[int] = Field(..., min_items=2, max_items=2)
    pupil: list[int] = Field(..., min_items=2)
    tutor: list[int] = Field(..., min_items=2)
