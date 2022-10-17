# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def f(my_list):
    my_list.sort(key=lambda x: x[1][-1])
    return my_list


l = [['abc', 'bcd'], ['abc', 'zza'], ['abc', 'zzb']]
print(f(l))
