import logging
from typing import List, Optional, Dict

# Enable debug logs so logging.debug(...) messages are shown
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def two_sum(number_list: List[int], target_value: int) -> Optional[List[int]]:
    logging.debug(f"Starting two_sum with nums = {nums}, target = {target}")

    # Dictionary to store number -> index
    seen: Dict[int, int] = {}

    for i, num in enumerate(number_list):
        logging.debug(f"Iteration start | index = {i} and num = {num}")

        complement = target_value - num
        logging.debug(f"Complement needed {complement}")

        # Check if complement is already exists
        if complement in seen:
            logging.debug(f"Complement found in seen at index {seen[complement]}")

            logging.debug(f"Returning result: [{seen[complement]}, {i}]")
            return [seen[complement], i]

        # Store number in dictionary
        seen[num] = i
        logging.debug(f"Added to seen: {num} -> index {i}")
        logging.debug(f"Current seen directory: {seen}")
    logging.debug(f"No pair found. Returning None")
    return None


class TwoSum:
    def __init__(self, nums_lst: List[int], target_val: int) -> None:
        logging.debug(f"Initializing TwoSum with nums={nums} and target={target}")
        self.nums_lst = nums_lst
        self.target_val = target_val

    def process(self) -> Optional[List[int]]:
        logging.debug(f"Calling two-sum function from TwoSum.process()")
        return two_sum(self.nums_lst, self.target_val)


if __name__ == "__main__":
    # Input data
    nums = [2, 7, 11, 15]
    target = 26

    # Create object for class
    two_sum_obj = TwoSum(nums, target)
    result = two_sum_obj.process()

    print("Result:", result)
