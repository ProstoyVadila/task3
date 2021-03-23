from typing import NamedTuple, Optional, List

from main import IntervalsModel


class TimeStamp(NamedTuple):
    start: int
    end: int


def create_timestamps(items: List[int]) -> List[TimeStamp]:
    list_ = []
    for i in range(1, len(items), 2):
        list_.append(TimeStamp(start=items[i-1], end=items[i]))
    return list_


def get_overlap(x_start: int, x_end: int, y_start: int, y_end: int) -> Optional[TimeStamp]:
    if x_start < y_end and y_start < x_end:
        start = max(x_start, y_start)
        end = min(x_end, y_end)
        return TimeStamp(start=start, end=end)
    else:
        return None


def get_sum_and_overlaps(x_list: List[TimeStamp], y_list: List[TimeStamp]) -> [List[TimeStamp], int]:
    overlaps = []
    sum_ = 0

    for x in x_list:
        for y in y_list:
            overlap = get_overlap(x.start, x.end, y.start, y.end)
            if overlap:
                overlaps.append(overlap)
                delta = overlap.end - overlap.start
            else:
                delta = 0
            sum_ += delta

    return overlaps, sum_


def appearance(intervals: IntervalsModel) -> int:
    lesson = create_timestamps(intervals.lesson)
    pupil = create_timestamps(intervals.pupil)
    tutor = create_timestamps(intervals.tutor)

    tut_pup_overlaps, _ = get_sum_and_overlaps(tutor, pupil)
    _, result_sum = get_sum_and_overlaps(tut_pup_overlaps, lesson)

    return result_sum
