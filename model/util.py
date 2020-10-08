import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    to_return = []
    small_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    capital_letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    allowed_special_chars = ["_", "+", "-", "!"]
    
    for i in range(0, number_of_small_letters):
        to_return.append(small_letters[random.randint(0, len(small_letters) - 1 ) ])
        # add_c = len(small_letters) - 1
        # add_b = random.randint(0, add_c )
        # add_a = small_letters[add_b ]
        # to_return.append( add_a)
    #print(to_return)

    for i in range(0, number_of_capital_letters):
        to_return.append(capital_letters[random.randint(0, len(capital_letters ) -1 )]  )
        # rtn_c = len(capital_letters ) -1
        # rtn_b = random.randint(0, rtn_c )
        # rtn_a = capital_letters[rtn_b]
        # to_return.append(rtn_a  )
    #print(to_return)

    for i in range(0, number_of_special_chars):
        to_return.append(allowed_special_chars[random.randint(0, len(allowed_special_chars ) - 1 )] )

        # rtn_c = len(allowed_special_chars ) - 1
        # rtn_b = random.randint(0, rtn_c )
        # rtn_a = allowed_special_chars[rtn_b]
        # to_return.append(rtn_a  )
    str_to_return = ""

    for i in range(0,len(to_return)):
        str_to_return += to_return[i]
    #print(str_to_return)

    return str_to_return


