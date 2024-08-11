# Annotated provides additional validation for the variables
# Mostly used with Fast API for context validation

# Custom Annotations
from typing import Annotated, get_type_hints, get_args


def apply_percent_condition(func):

    def check_percentage(number: int, percentage: int):
        type_hints = get_type_hints(func, include_extras=True)
        hints = type_hints['percentage']
        _, *hint_args = get_args(hints)
        low = hint_args[0][0]
        hi = hint_args[0][1]
        if low <= percentage <= hi:
            return func(number, percentage)
        raise ValueError(f'Value should be between {low} and {hi}')
    return check_percentage


@apply_percent_condition
def get_percentage_of_number(number: int, percentage: Annotated[int, (0, 100)]) -> float:
    # Annotated[int, (0, 100)] just provides the metadata for validation and does nothing
    return (number * percentage)/100


number = int(input("Enter Number"))
percentage = int(input("Enter percentage"))
print(get_percentage_of_number(number, percentage))