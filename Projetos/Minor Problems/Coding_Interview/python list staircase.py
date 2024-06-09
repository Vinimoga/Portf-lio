def is_staircase(nums):
    col_length = 0
    staircase = []
    input_list = nums.copy()

    while len(input_list) > 0:
        col_length = col_length + 1
        column = []

        for i in range(0, col_length):
            column.append(input_list.pop(0))

            if (len(input_list) == 0):
                if i < col_length - 1:
                    return False
        staircase.append(f"{column}")

    return staircase

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
stair = is_staircase(nums)
for step in stair:
    print(step)