import unittest
def treatment_sum(our_tuple):
    try:
        if len(our_tuple) == 2:
            one, two = our_tuple
            result = one + two
            return result
        elif len(our_tuple) < 2:
            return 'Недостаточно данных'
        else:
            raise Exception('Много данных')
    except TypeError:
        return 'Нельзя сложить эти данные'

""""
def treatment_sum(input_tuple):
    if len(input_tuple) > 2:
        raise Exception('Много данных')
    elif len(input_tuple) < 2:
        return 'Недостаточно данных'
    else:
        try:
            return sum(input_tuple)
        except TypeError:
            return 'Нельзя сложить эти данные'

"""

d_tuple = (1, 2, 4)
print(treatment_sum(d_tuple))
