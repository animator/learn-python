import random
from box import Box
from typing import List


def line_boxes(mat, line) -> List[Box]:
    p1, p2 = line
    boxes = []
    if p1[0] == p2[0]:  # horizontal
        pos1 = min(p1, p2, key=lambda x: x[1])
        if pos1[0] > 0:
            box_top = mat[pos1[0] - 1][pos1[1]]
            boxes.append(box_top)
        if pos1[0] < len(mat):
            box_bottom = mat[pos1[0]][pos1[1]]
            boxes.append(box_bottom)
    else:
        pos1 = min(p1, p2, key=lambda x: x[0])
        if pos1[1] > 0:
            box_left = mat[pos1[0]][pos1[1] - 1]
            boxes.append(box_left)
        if pos1[1] < len(mat[0]):
            box_right = mat[pos1[0]][pos1[1]]
            boxes.append(box_right)
    return boxes


def get_boxes_around(box_mat, box: Box):
    boxes = {'top': None, 'bottom': None, 'left': None, 'right': None}
    if box.idx[0] > 0:
        boxes['top'] = box_mat[box.idx[0] - 1][box.idx[1]]
    if box.idx[0] < len(box_mat) - 1:
        boxes['bottom'] = box_mat[box.idx[0] + 1][box.idx[1]]
    if box.idx[1] > 0:
        boxes['left'] = box_mat[box.idx[0]][box.idx[1] - 1]
    if box.idx[1] < len(box_mat[0]) - 1:
        boxes['right'] = box_mat[box.idx[0]][box.idx[1] + 1]
    return boxes


def num_boxes_around(box_mat, box: Box):
    count = 0
    if box.idx[0] > 0:
        count += 1
    if box.idx[0] < len(box_mat) - 1:
        count += 1
    if box.idx[1] > 0:
        count += 1
    if box.idx[1] < len(box_mat[0]) - 1:
        count += 1
    return count


def get_empty(box):
    if box.top is None:
        return box.top_idx()
    elif box.bottom is None:
        return box.bottom_idx()
    elif box.left is None:
        return box.left_idx()
    else:
        return box.right_idx()


def get_rand_empty(box, exclude=None):
    choices = []
    if box.top is None:
        if exclude is None or box.top_idx() != exclude:
            choices.append(box.top_idx())
    if box.bottom is None:
        if exclude is None or box.bottom_idx() != exclude:
            choices.append(box.bottom_idx())
    if box.left is None:
        if exclude is None or box.left_idx() != exclude:
            choices.append(box.left_idx())
    if box.right is None:
        if exclude is None or box.right_idx() != exclude:
            choices.append(box.right_idx())
    return random.choice(choices)


def get_sides_box(box_mat, box: Box):
    sides = {'top': None, 'bottom': None, 'left': None, 'right': None}
    if box.idx[0] > 0:
        sides['top'] = box_mat[box.idx[0] - 1][box.idx[1]].sides
    if box.idx[0] < len(box_mat) - 1:
        sides['bottom'] = box_mat[box.idx[0] + 1][box.idx[1]].sides
    if box.idx[1] > 0:
        sides['left'] = box_mat[box.idx[0]][box.idx[1] - 1].sides
    if box.idx[1] < len(box_mat[0]) - 1:
        sides['right'] = box_mat[box.idx[0]][box.idx[1] + 1].sides
    return sides


def less_than_sides(box_mat, box: Box, side, num):
    sides = get_sides_box(box_mat, box)[side]
    if side == 'top' and box.top is not None:
        return False
    if side == 'bottom' and box.bottom is not None:
        return False
    if side == 'left' and box.left is not None:
        return False
    if side == 'right' and box.right is not None:
        return False
    if sides is None:
        return True
    return sides < num


def facing_out(box_mat, box: Box):
    if box.idx[0] == 0 and box.top is None:
        return True
    if box.idx[0] == len(box_mat) - 1 and box.bottom is None:
        return True
    if box.idx[1] == 0 and box.left is None:
        return True
    if box.idx[1] == len(box_mat[0]) - 1 and box.right is None:
        return True
    return False


def easy(box_mat, prev_line):
    if prev_line is not None:
        prev_boxes = line_boxes(box_mat, prev_line)

        for prev_box in prev_boxes:
            if prev_box.sides == 3:
                return get_rand_empty(prev_box)

    boxes = Box.ALL_BOXES
    box0 = list(filter(lambda x: x.sides == 0, boxes))
    box1 = list(filter(lambda x: x.sides == 1, boxes))
    box2 = list(filter(lambda x: x.sides == 2, boxes))
    box3 = list(filter(lambda x: x.sides == 3, boxes))

    if box3:
        return get_rand_empty(random.choice(box3))
    if box0:
        return get_rand_empty(random.choice(box0))
    if box1:
        return get_rand_empty(random.choice(box1))
    if box2:
        return get_rand_empty(random.choice(box2))


def medium(box_mat, prev_line):
    if prev_line is not None:
        prev_boxes = line_boxes(box_mat, prev_line)

        for prev_box in prev_boxes:
            if prev_box.sides == 3:
                return get_rand_empty(prev_box)

    boxes = Box.ALL_BOXES
    box0 = list(filter(lambda x: x.sides == 0, boxes))
    box1 = list(filter(lambda x: x.sides == 1, boxes))
    box2 = list(filter(lambda x: x.sides == 2, boxes))
    box3 = list(filter(lambda x: x.sides == 3, boxes))

    box_less2 = box0 + box1

    if box3:
        return get_rand_empty(random.choice(box3))

    top = list(filter(lambda x: less_than_sides(box_mat, x, 'top', 2), box_less2))
    bottom = list(filter(lambda x: less_than_sides(box_mat, x, 'bottom', 2), box_less2))
    left = list(filter(lambda x: less_than_sides(box_mat, x, 'left', 2), box_less2))
    right = list(filter(lambda x: less_than_sides(box_mat, x, 'right', 2), box_less2))
    choices = []
    choices.extend([i.top_idx() for i in top])
    choices.extend([i.bottom_idx() for i in bottom])
    choices.extend([i.left_idx() for i in left])
    choices.extend([i.right_idx() for i in right])
    if choices:
        return random.choice(choices)

    if box0:
        return get_rand_empty(random.choice(box0))
    if box1:
        return get_rand_empty(random.choice(box1))
    if box2:
        return get_rand_empty(random.choice(box2))


def hard(box_mat, prev_line):
    if prev_line is not None:
        prev_boxes = line_boxes(box_mat, prev_line)

        for prev_box in prev_boxes:
            if prev_box.sides == 3:
                return get_rand_empty(prev_box)

    boxes = Box.ALL_BOXES
    box0 = list(filter(lambda x: x.sides == 0, boxes))
    box1 = list(filter(lambda x: x.sides == 1, boxes))
    box3 = list(filter(lambda x: x.sides == 3, boxes))

    if box3:
        return get_rand_empty(random.choice(box3))

    box_less2 = box0 + box1

    top = list(filter(lambda x: less_than_sides(box_mat, x, 'top', 2), box_less2))
    bottom = list(filter(lambda x: less_than_sides(box_mat, x, 'bottom', 2), box_less2))
    left = list(filter(lambda x: less_than_sides(box_mat, x, 'left', 2), box_less2))
    right = list(filter(lambda x: less_than_sides(box_mat, x, 'right', 2), box_less2))
    choices = []
    choices.extend([i.top_idx() for i in top])
    choices.extend([i.bottom_idx() for i in bottom])
    choices.extend([i.left_idx() for i in left])
    choices.extend([i.right_idx() for i in right])
    if choices:
        return random.choice(choices)

    chains = []
    checked = []
    crosses = []
    options = boxes.copy()
    while len(checked) < len(boxes):
        current = [options[0]]
        if current[0].color is not None:
            checked.append(current[0])
            options.remove(current[0])
            continue
        if current[0].sides < 2:
            crosses.append(current[0])
            checked.append(current[0])
            options.remove(current[0])
            continue
        new = []
        chain = []
        while current:
            for box in current:
                checked.append(box)
                chain.append(box)
                options.remove(box)
                around = get_boxes_around(box_mat, box)
                if box.top is None and around['top'] is not None:
                    if around['top'] not in new and around['top'] not in chain:
                        if around['top'].sides >= 2:
                            new.append(around['top'])
                if box.bottom is None and around['bottom'] is not None:
                    if around['bottom'] not in new and around['bottom'] not in chain:
                        if around['bottom'].sides >= 2:
                            new.append(around['bottom'])
                if box.left is None and around['left'] is not None:
                    if around['left'] not in new and around['left'] not in chain:
                        if around['left'].sides >= 2:
                            new.append(around['left'])
                if box.right is None and around['right'] is not None:
                    if around['right'] not in new and around['right'] not in chain:
                        if around['right'].sides >= 2:
                            new.append(around['right'])
            current = new
            new = []
        chains.append(chain)

    sorted_chains = sorted(chains, key=lambda x: len(x))

    if sorted_chains:
        return get_rand_empty(random.choice(sorted_chains[0]))

    return get_rand_empty(random.choice(crosses))


def extreme(box_mat, prev_line):
    boxes = Box.ALL_BOXES
    box0 = list(filter(lambda x: x.sides == 0, boxes))
    box1 = list(filter(lambda x: x.sides == 1, boxes))
    box3 = list(filter(lambda x: x.sides == 3, boxes))

    box_less2 = box0 + box1

    top = list(filter(lambda x: less_than_sides(box_mat, x, 'top', 2), box_less2))
    bottom = list(filter(lambda x: less_than_sides(box_mat, x, 'bottom', 2), box_less2))
    left = list(filter(lambda x: less_than_sides(box_mat, x, 'left', 2), box_less2))
    right = list(filter(lambda x: less_than_sides(box_mat, x, 'right', 2), box_less2))
    choices = []
    choices.extend([i.top_idx() for i in top])
    choices.extend([i.bottom_idx() for i in bottom])
    choices.extend([i.left_idx() for i in left])
    choices.extend([i.right_idx() for i in right])

    chains = []
    checked = []
    crosses = []
    options = boxes.copy()
    while len(checked) < len(boxes):
        current = [options[0]]
        if current[0].color is not None:
            checked.append(current[0])
            options.remove(current[0])
            continue
        if current[0].sides < 2:
            crosses.append(current[0])
            checked.append(current[0])
            options.remove(current[0])
            continue
        new = []
        chain = []
        while current:
            for box in current:
                checked.append(box)
                chain.append(box)
                options.remove(box)
                around = get_boxes_around(box_mat, box)
                if box.top is None and around['top'] is not None:
                    if around['top'] not in new and around['top'] not in chain:
                        if around['top'].sides >= 2:
                            new.append(around['top'])
                if box.bottom is None and around['bottom'] is not None:
                    if around['bottom'] not in new and around['bottom'] not in chain:
                        if around['bottom'].sides >= 2:
                            new.append(around['bottom'])
                if box.left is None and around['left'] is not None:
                    if around['left'] not in new and around['left'] not in chain:
                        if around['left'].sides >= 2:
                            new.append(around['left'])
                if box.right is None and around['right'] is not None:
                    if around['right'] not in new and around['right'] not in chain:
                        if around['right'].sides >= 2:
                            new.append(around['right'])
            current = new
            new = []
        chains.append(chain)

    sorted_chains = sorted(chains, key=lambda x: len(x))

    if prev_line is not None:
        prev_boxes = line_boxes(box_mat, prev_line)

        for prev_box in prev_boxes:
            if prev_box.sides == 3:
                side = get_rand_empty(prev_box)
                if not choices and len(sorted_chains) > 1:
                    if len(sorted_chains[1]) > 2 and len(box3) < 2:
                        side_boxes = line_boxes(box_mat, side)
                        for box in side_boxes:
                            if box != prev_box:
                                if num_boxes_around(box_mat, box) < 4 and facing_out(box_mat, box):
                                    return get_rand_empty(box, exclude=side)
                return side

    if box3:
        b = random.choice(box3)
        side = get_rand_empty(b)
        if not choices and len(sorted_chains) > 1:
            if len(sorted_chains[1]) > 2 and len(box3) < 2:
                side_boxes = line_boxes(box_mat, side)
                for box in side_boxes:
                    if box != b:
                        if num_boxes_around(box_mat, box) < 4 and facing_out(box_mat, box):
                            return get_rand_empty(box, exclude=side)
        return side

    if choices:
        return random.choice(choices)

    if sorted_chains:
        return get_rand_empty(random.choice(sorted_chains[0]))

    return get_rand_empty(random.choice(crosses))


def expert(box_mat, prev_line):
    pass  # coming soon


class Player:
    def __init__(self, player_type, color, difficulty=1):
        self.player_type = player_type
        self.score = 0
        self.color = color
        self.start = None
        self.move = None
        self.difficulty = difficulty

    def get_move(self, box_mat, prev_line):
        if self.player_type == 'human':
            m = self.move
            self.move = None
            return m

        if self.difficulty == 1:
            return easy(box_mat, prev_line)
        elif self.difficulty == 2:
            return medium(box_mat, prev_line)
        elif self.difficulty == 3:
            return hard(box_mat, prev_line)
        elif self.difficulty == 4:
            return extreme(box_mat, prev_line)
