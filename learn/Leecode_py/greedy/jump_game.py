def jump_game(arr):
    # for zero_idx, ele in enumerate(arr):
    #     if ele == 0:
    #         can_jump = False
    #         for id, el in enumerate(arr[0:zero_idx]):
    #             can_jump |= (zero_idx - id) < el
    #         if not can_jump:
    #             return False
    reached = arr[0]

    for idx, ele in enumerate(arr):
        if reached < idx:
            return False
        reached = max(reached, ele + idx)

    return reached >= len(arr) - 1


if __name__ == "__main__":
    arrs = [[0], [0, 1, 2, 5], [1, 1, 0, 5], [1], [1, 1, 1, 1, 1],
            [2, 3, 1, 1, 4], [3, 2, 1, 0, 4]]
    res = [True, False, False, True, True, True, False]

    for idx, test in enumerate(arrs):
        print(res[idx] == jump_game(test))
