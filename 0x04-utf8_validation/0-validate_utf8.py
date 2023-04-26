#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: a list of integers representing the bytes of the data set
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    # Number of bytes remaining in the current UTF-8 character
    bytes_remaining = 0

    # Iterate through each byte in the data set
    for byte in data:
        # Check if this byte is the start of a new UTF-8 character
        if bytes_remaining == 0:
            # Determine the number of bytes in this UTF-8 character
            if byte >> 7 == 0b0:
                # Character is 1 byte long
                bytes_remaining = 0
            elif byte >> 5 == 0b110:
                # Character is 2 bytes long
                bytes_remaining = 1
            elif byte >> 4 == 0b1110:
                # Character is 3 bytes long
                bytes_remaining = 2
            elif byte >> 3 == 0b11110:
                # Character is 4 bytes long
                bytes_remaining = 3
            else:
                # Invalid UTF-8 character start byte
                return False
        else:
            # This byte should be a continuation byte
            if byte >> 6 != 0b10:
                # Invalid UTF-8 continuation byte
                return False
            bytes_remaining -= 1
    return bytes_remaining == 0
