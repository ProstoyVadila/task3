from fastapi import FastAPI

from models import IntervalsModel
from task import appearance


app = FastAPI(title='Task_3')


@app.post(
    '/appearance',
    description='Post intervals data to get appearance time'
)
async def get_appearance(intervals: IntervalsModel):
    res = appearance(intervals)
    return {
        'sum_of_appearances': res
    }
