import random
import string


def generate_id(number_of_small_letters=4, number_of_capital_letters=2, number_of_digits=2, number_of_special_chars=2, allowed_special_chars=r"_+-!"):

    random_elements_of_id = []
    result_id = ""

    for _ in range(number_of_small_letters):
        random_elements_of_id.append(random.choice(string.ascii_lowercase))
    for _ in range(number_of_capital_letters):
        random_elements_of_id.append(random.choice(string.ascii_uppercase))
    for _ in range(number_of_digits):
        random_elements_of_id.append(random.choice(range(0, 10)))
    for _ in range(number_of_special_chars):
        random_elements_of_id.append(random.choice(allowed_special_chars))

    random.shuffle(random_elements_of_id)

    for element in random_elements_of_id:
        element = str(element)
        result_id += element

    return result_id
