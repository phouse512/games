from typing import List

def is_empty_row(row: List[str]) -> bool:
    any_empty = False  # type: bool
    for i in row:
        any_empty = bool(any_empty or i)

    return not any_empty
