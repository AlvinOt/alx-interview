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
