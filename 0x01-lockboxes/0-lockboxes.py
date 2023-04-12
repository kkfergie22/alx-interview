#!/usr/bin/python3
"""Module for the function canUnlockAll(boxes)."""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    if not boxes:
        return False
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = boxes[0]
    for i in range(len(boxes)):
        if (unlocked[i]):
            for key in boxes[i]:
                if key < len(boxes) and not unlocked[key]:
                    unlocked[key] = True
                    keys.append(key)
    return all(unlocked)
