'''
The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary 
that has strings as keys and values) and a dictionary. 
A rule is defined as follows: (key, "prefix", "middle", "suffix"). 
A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) 
and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.

Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and 
d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are respected 
for "key1" and "key2" "key3" that does not appear in the rules.
'''

s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside , it's too cold out",
     "key2": "start this middle is not valid winter"}


def check_prefix(seq, my_string):
    if seq == '':
        return True
    if my_string.find(seq) == 0:
        return True
    # my_string = my_string.split()
    # if my_string[0] == seq:
    #     return True
    return False


def check_sufix(seq, my_string):
    if seq == '':
        return True
    if my_string.find(seq) == len(my_string) - len(seq):
        return True
    # my_string = my_string.split()
    # if my_string[-1] == seq:
    #     return True
    return False


def check_inside(seq, my_string):
    if seq == '':
        return True

    if my_string.find(seq) > 0 and my_string.find(seq) < len(my_string) - len(seq) - 1:
        return True
    # my_string = my_string.split()
    # for index, word in enumerate(my_string):
    #     if word == seq and index > 0 and index < len(my_string) - 1:
    #         return True
    return False


def validate_dict(s, d):
    for i in s:
        x = d.get(i[0])
        if x is None:
            return False
        if check_prefix(i[1], x) == False or check_inside(i[2], x) == False or check_sufix(i[3], x) == False:
            print(check_prefix(i[1], x), check_inside(
                i[2], x), check_sufix(i[3], x), i, x)
            return False
    return True

# seq = "da"
# my_string = "nu x am zi x x da"

# print(check_prefix(seq, my_string))
# print(check_sufix(seq, my_string))
# print(check_inside(seq, my_string))


print(validate_dict(s, d))
