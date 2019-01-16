def remove_element(arr, value):
    """  Go through the array,
         set two pointers,
         one pointer moves normally,
         another pointer moves depends on the equal value
    """
    length = len(arr)
    one_p = 0
    two_p = 0

    while one_p < length:
        if arr[two_p] == value:
            one_p += 1
        else:
            arr[two_p] = arr[one_p]
            one_p += 1
            two_p += 1
    return arr
