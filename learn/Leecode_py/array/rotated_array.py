def rotated_point(rotated_array):
    """Fix one end,use binary search. Swap the start and the end when finds the rotated area"""
    start = 0
    end = len(rotated_array)
    if end == 1:
        return 0
    if end == 0:
        return -1
    while start < end:
