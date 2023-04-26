#!/usr/bin/python3

""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing a data set.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check if the most significant bit (MSB) is set or not
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Check each byte in the data set
    for byte in data:
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Check how many bytes this UTF-8 character contains
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If this is not a valid UTF-8 character, return False
            if num_bytes == 0:
                continue

            # If this is a one-byte UTF-8 character, no need to check further
            if num_bytes == 1:
                continue
        else:
            # If this is not a continuation byte, return False
            if not (byte & mask1 and byte & mask2):
                return False

        # We've read a valid continuation byte
        num_bytes -= 1

    # If there are no more continuation bytes expected, the data is valid UTF-8
    return num_bytes == 0
