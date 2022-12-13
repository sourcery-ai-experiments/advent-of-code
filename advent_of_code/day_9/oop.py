"""
OOP solution for day 9.
"""
from __future__ import annotations

import enum
from typing import Any


# noinspection DuplicatedCode
class Position(tuple):
    """
    A position on a ZxZ plane.
    """
    def __new__(cls, *args):
        return super(Position, cls).__new__(cls, args)

    def __add__(self, other: Position | tuple[int, ]):
        other = Position.from_tuple(other) if isinstance(other, tuple) else other
        length = max(len(self), len(other))

        return Position(
            *(self.get(index_) + other.get(index_) for index_ in range(length))
        )

    def __radd__(self, other: Position | tuple[int, ]):
        return self.__add__(other)

    def __iadd__(self, other: Position | tuple[int, ]):
        return self.__add__(other)

    def __sub__(self, other):
        other = Position.from_tuple(other) if isinstance(other, tuple) else other
        length = max(len(self), len(other))

        return Position(
            *(self.get(index_) - other.get(index_) for index_ in range(length))
        )

    def __rsub__(self, other: Position | tuple[int, ]):
        return self.__sub__(other)

    def __isub__(self, other: Position | tuple[int, ]):
        return self.__sub__(other)

    def get(self, index_: int) -> Any:
        """
        Get the value at the index, returning 0 if the index does not exist.
        """
        if index_ < 0 or not isinstance(index_, int):
            raise IndexError(f"Position index {index_} is out of range")

        try:
            return self[index_]
        except IndexError:
            return 0

    @classmethod
    def from_tuple(cls, tuple_: tuple) -> Position:
        """
        Construct a Position from a tuple.
        """
        return cls(*iter(tuple_))


# Math co-ordinates
UP = Position(0, 1)
DOWN = Position(0, -1)
LEFT = Position(-1, 0)
RIGHT = Position(1, 0)
DIRECTIONS = {
    "U": UP,
    "D": DOWN,
    "L": LEFT,
    "R": RIGHT,
}


class Rope:
    """
    A rope, whose head has a position and whose tail has a position.
    """
    def __init__(self, starting_position: Position, knots: int):
        """
        Create a rope with a starting position and some number of knots.
        """
        self._head_position = starting_position
        self._tail_position = starting_position

        self.knots = knots
        self.knot_positions: dict[int, Position] = {
            i: starting_position
            for i in range(knots)
        }

        self.head_position_history = [starting_position]
        self.tail_position_history = [starting_position]

    def __str__(self):
        return f"head={self.head_position}, tail={self.tail_position}"

    @property
    def head_position(self) -> Position:
        """
        The head's position.
        """
        return self._head_position

    @head_position.setter
    def head_position(self, value: Position) -> None:
        """
        Set the head's position.
        """
        self._head_position = value
        self.head_position_history.append(value)

    @property
    def tail_position(self) -> Position:
        """
        The tail's position.
        """
        return self._tail_position

    @tail_position.setter
    def tail_position(self, value: Position) -> None:
        """
        Set the tail's position.
        """
        self._tail_position = value
        self.tail_position_history.append(value)

    def resolve_tail_position(self) -> None:
        """
        Update the tail position to correctly follow the head around.

        TODO: This depends on the number of knots in a different way. Need to
        resolve them in order.
        """
        x, y = (self.head_position - self.tail_position)
        if abs(x) == 2:
            self.tail_position += Position(x / 2, y)
        elif abs(y) == self.knots:
            self.tail_position += Position(x, y / 2)
        else:
            ValueError(f"Larger distance than expected, found {x, y=}")

    def move(self, direction: str) -> None:
        """
        Move the head of the rope, and subsequently the tail of the rope if
        necessary.
        """
        self.head_position += DIRECTIONS[direction]
        self.resolve_tail_position()

    def follow_instructions(self, instructions: list[str]) -> None:
        """
        Follow the instructions given, which are to move in different directions
        by various amounts.
        """
        for instruction in instructions:
            direction, quantity = instruction.split()
            for _ in range(int(quantity)):
                self.move(direction)


def solution(input_: str) -> list[Any]:
    """
    Solve the day 9 problem!
    """
    rope_1 = Rope(starting_position=Position(0, 0), knots=2)
    rope_1.follow_instructions(instructions=input_.strip().split("\n"))
    rope_2 = Rope(starting_position=Position(0, 0), knots=10)
    rope_2.follow_instructions(instructions=input_.strip().split("\n"))

    return [
        len(set(rope_1.tail_position_history)),
        len(set(rope_2.tail_position_history)),
    ]
