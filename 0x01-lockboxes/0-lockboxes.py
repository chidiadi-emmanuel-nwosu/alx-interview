#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""

    keys = set(boxes[0])
    for idx in range(1, len(boxes)):
        if idx in keys:
            keys |= set(boxes[idx])
        else:
            tmp = set()
            for key in keys:
                if key < len(boxes):
                    tmp |= set(boxes[key])
            if idx not in tmp:
                return False

    return True
