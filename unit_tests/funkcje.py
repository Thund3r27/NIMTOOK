import string

def is_palindrome(text: str) -> bool:
    cleaned = "".join(char.lower() for char in text if char != " ")
    return cleaned == cleaned[::-1]

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Ciąg Fibonacciego nie jest zdefiniowany dla liczb ujemnych.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def count_vowels(text: str) -> int:
    vowels = set("aeiouyAEIOUY")
    return sum(1 for char in text if char in vowels)

def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Zniżka musi mieścić się w przedziale od 0 do 1.")
    return float(price * (1 - discount))

def flatten_list(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def word_frequencies(text: str) -> dict:
    if not text:
        return {}

    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.translate(translator).lower()

    words = cleaned_text.split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
