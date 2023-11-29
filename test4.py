from functools import reduce


def find_missing_element(full_list, partial_list):
    return reduce(lambda a, b: a ^ b, full_list) ^ reduce(lambda a, b: a ^ b, partial_list)


def find_missing_element2(full_list, partial_list):
    output = 0
    for num in (*full_list, *partial_list):
        output ^= num
    return output


def find_missing_element3(full_list, partial_list):
    return [x for x in full_list if x not in partial_list]


lst1 = [4, 9, 5, 3, 2]
lst2 = [5, 4, 9, 2]
print(find_missing_element(lst1, lst2))
print(find_missing_element2(lst1, lst2))
print(find_missing_element3(lst1, lst2))


def first_missing(string):
    new_dict = dict()
    for ch in string:
        if ch not in new_dict:
            new_dict[ch] = 1
        else:
            new_dict[ch] += 1

    for ch in string:
        if new_dict[ch] == 1:
            return ch
    return '_'


def max_subarray_sum(array):
    current_sum = max_sum = 0
    for num in array:
        if num > current_sum + num:
            current_sum = num
        else:
            current_sum += num
        if max_sum < current_sum:
            max_sum = current_sum

    return max_sum


print(max_subarray_sum([1, -2, 4, -3, 12, -1, 0]))
print(max_subarray_sum([-2, 2, 5, -11, 6]))
