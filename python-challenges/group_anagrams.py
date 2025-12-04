"""
O(N·K) Optimized - Group-Anagrams

N - number of strings
K - maximum length of a string
For each string we compute a frequency count of 26 letters - O(K)
Total - O(N.K)
Used a dictionary with tuple keys - avoids sorting (which would be O(K log K))
"""
import logging
from typing import List, Dict, Tuple

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def group_anagrams(str_lst: List[str]) -> List[List[str]]:
    logging.debug(f"Input list: {str_lst}")

    # Dictionary: key - 26 letter frequency tuple, value - list of anagrams
    anagram_map: Dict[Tuple[int, ...], List[str]] = {}

    for word in str_lst:
        logging.debug(f"Processing string/word: {word}")

        # Build frequency count of 26 characters
        char_count_list: List[int] = [0] * 26
        for ch in word:
            char_index: int = ord(ch) - ord('a')
            char_count_list[char_index] += 1
            logging.debug(f"Character '{ch}' -> index {char_index} updated count = {char_count_list}")

        key: Tuple[int, ...] = tuple(char_count_list)
        logging.debug(f"Computed kay for '{word}': {key}")

        # Append string to its anagram group
        if key not in anagram_map:
            anagram_map[key]: Tuple[int, ...] = []
            logging.debug(f"Created new group for key {key}")

        anagram_map[key].append(word)
        logging.debug(f"Added '{word}' to group {anagram_map[key]}")

        # Final grouped anagrams
        logging.debug(f"Final grouped anagrams")
        for k, v in anagram_map.items():
            logging.debug(f"Key={k} -> Group={v}")

    logging.debug(f"final anagram_map dictionary: {anagram_map}")
    grouped_anagrams: List[List[str]] = list(anagram_map.values())

    return grouped_anagrams


class GroupAnagrams:
    def __init__(self, str_lst: List[str]) -> None:
        self.str_lst = str_lst

    def process(self) -> List[List[str]]:
        return group_anagrams(self.str_lst)


if __name__ == "__main__":
    # Input data
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    # Create class object
    group_anagrams_obj = GroupAnagrams(strs)
    result: List[List[str]] = group_anagrams_obj.process()

    # Display the result
    print(result)
