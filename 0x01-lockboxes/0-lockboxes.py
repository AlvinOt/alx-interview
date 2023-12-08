#!/usr/bin/python3
"""You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other
boxes.
Write a method that determines if all the boxes can be opened."""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    :param boxes: List of lists, each containing keys to other boxes.
    :return: True if all boxes can be opened, else False.
    """

    opened_boxes = {0}

    boxes_to_check = [0]

    while boxes_to_check:
        current_box = boxes_to_check.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                boxes_to_check.append(key)

    return len(opened_boxes) == len(boxes)
