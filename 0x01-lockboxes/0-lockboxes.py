#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""

    if not isinstance(boxes, list) or any(not isinstance(box, list) for box in boxes):
        return False

    keys = set(boxes[0])
    for idx in range(1, len(boxes)):
        if idx in keys:
            keys |= set(list(boxes[idx]))
        else:
            tmp = set([])
            for key in keys:
                tmp |= set(list(boxes[key]))
            if idx not in tmp:
                return False

    return True
