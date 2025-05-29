def get_num_words(text: str) -> int:
    return len(text.split())

def get_char_count(text: str) -> dict[str, int]:
    counter = {}
    for char in text.lower():
        if char not in counter: 
            counter[char] = 1
        else:
            counter[char] += 1
    return counter 

def create_sorted_list(counter: dict[str, int]) -> list[dict]:
    sorted_list = [{"char": key, "num": value} for key, value in counter.items()]
    return sorted_list

