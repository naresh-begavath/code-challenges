"""
Question:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

MOTO: Handle duplicates like in log aggregation

Steps to produce solution:
input -> nums = [-1, 0, 1, 2, -1, -4]
output -> [-1, -1, 2], [-1, 0, 1]

Step1: Sort the array.
Sorting helps remove duplicates and use two pointer technique efficiently.
[-4, -1, 0, 1, 2]

Step2: Fix one number at index i
For each number at i, we try to find other numbers that form sum = - nums[i]

Step3: Use two-pointers
left pointer = i + 1
right pointer = len(nums) - 1

Then we compute,
current_sum = nums[i] + nums[left] + nums[right]

Move pointer:
    if sum < 0 -> then need bigger number -> move left -> left + 1
    if sum > 0 -> then need smaller number -> move right -> right + 1
    if sum == 0 -> valid triplet

"""
import logging
from typing import List

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def find_three_sum(nums_lst: List[int]) -> list[list[int]]:
    logging.debug(f"Input list: {nums_lst}\n")

    # Sort the given array
    nums_lst.sort()
    logging.debug(f"Sorted input list: {nums_lst}\n")

    # Declare a list variable to store result
    result_list: List[List[int]] = []

    for i in range(len(nums_lst)):
        # Avoid duplicate fixed numbers
        if i > 0 and nums_lst[i] == nums_lst[i - 1]:
            logging.debug(f"Skipp duplicate at i = {i}, nums_lst[i]=={nums_lst[i]}\n")
            continue

        left: int = i + 1
        right: int = len(nums_lst) - 1
        logging.debug(f"Fixing nums_lst[i] at index i = {i}\n")

        while left < right:
            current_sum = nums_lst[i] + nums_lst[left] + nums_lst[right]
            logging.debug(
                f"Checking i = {i}, left = {left}, right = {right} -> "
                f"({nums_lst[i]}, {nums_lst[left]}, {nums_lst[right]}) sum = {current_sum}\n"
            )

            if current_sum < 0:
                logging.debug(f"Sum < 0 -> moving left pointer\n")
                left += 1
            elif current_sum > 0:
                logging.debug(f"Sum > 0 -> moving right pointer\n")
                right -= 1
            else:
                logging.debug(f"Found triplet\n")
                result_list.append([nums_lst[i], nums_lst[left], nums_lst[right]])

                # Skip duplicate for left pointers
                left_val = nums_lst[left]
                while left < right and nums_lst[left] == left_val:
                    logging.debug(f"Skipping duplicates after match at left = {left}\n")
                    left += 1

                # Skip duplicates for right pointer
                right_val = nums_lst[right]
                while left < right and nums_lst[right] == right_val:
                    logging.debug(f"Skipping duplicate after match at right = {right}\n")
                    right -= 1

    return result_list


class ThreeSum:
    def __init__(self, nums_lst: List[int]) -> None:
        self.nums_lst = nums_lst

    def process(self) -> List[List[int]]:
        return find_three_sum(self.nums_lst)


if __name__ == "__main__":
    # Input data
    input_nums_lst: List[int] = [-1, 0, 1, 2, -1, -4]

    # Create class object
    three_sum = ThreeSum(input_nums_lst)
    result: List[List[int]] = three_sum.process()

    # Display the output
    print(result)
