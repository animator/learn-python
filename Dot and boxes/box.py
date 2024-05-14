from typing import List


class Box:
    ALL_BOXES: List["Box"] = []
    BOXES_DONE = 0

    def __init__(self, y, x):
        self.idx = y, x
        self._top = None
        self._bottom = None
        self._left = None
        self._right = None
        self.sides = 0
        self.color = None

        Box.ALL_BOXES.append(self)

    def top_idx(self):
        return self.idx, (self.idx[0], self.idx[1] + 1)

    def bottom_idx(self):
        return (self.idx[0] + 1, self.idx[1]), (self.idx[0] + 1, self.idx[1] + 1)

    def left_idx(self):
        return self.idx, (self.idx[0] + 1, self.idx[1])

    def right_idx(self):
        return (self.idx[0], self.idx[1] + 1), (self.idx[0] + 1, self.idx[1] + 1)

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, top):
        self._top = top
        self.sides += 1
        if self.sides == 4:
            self.color = top
            Box.BOXES_DONE += 1

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        self._bottom = bottom
        self.sides += 1
        if self.sides == 4:
            self.color = bottom
            Box.BOXES_DONE += 1

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left
        self.sides += 1
        if self.sides == 4:
            self.color = left
            Box.BOXES_DONE += 1

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right
        self.sides += 1
        if self.sides == 4:
            self.color = right
            Box.BOXES_DONE += 1
