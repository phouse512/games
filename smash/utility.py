from typing import List

def is_empty_row(row: List[str]) -> bool:
    any_empty = False  # type: bool
    for i in row:
        any_empty = bool(any_empty or i)

    return not any_empty


def time_difference_to_int(start_time: str, end_time: str) -> int:
    """ this method takes a start time and end time in the format "mm:ss"
            and subtracts them to return the integer difference in seconds
    """

    start_values = start_time.split(":")
    start_minute = int(start_values[0])
    start_seconds = int(start_values[1])

    end_values = end_time.split(":")
    end_minute = int(end_values[0])
    end_seconds = int(end_values[1])

    minute_diff = start_minute - end_minute
    second_diff = start_seconds - end_seconds

    return (60 * minute_diff + second_diff)

