def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if int(num) > 0]


def choose_func(nums, func1, func2):
    numbers_of_negative = 0
    try:
        for num in nums:
            if num < 0:
                numbers_of_negative += 1
        if numbers_of_negative == 0:
            return func1(nums)
        else:
            return func2(nums)
    except TypeError or ValueError:
        print('У вашому списку є некоректні дані. Перевірте, будь ласка.')


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

print(choose_func(nums1, square_nums, remove_negatives))  # [1, 4, 9, 16, 25]
print(choose_func(nums2, square_nums, remove_negatives))  # [1, 3, 5]
