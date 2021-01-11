# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    # Write code here
    if type(l) != list:
        raise TypeError('Must be entered as list')
    if len(l) < 1:
        raise ValueError('List must contain at least one index')
    if len(l) == 1:
        return l[0]
    else:
        max_value = find_max(l[1:])
        if max_value > l[0]:
            return max_value
        else:
            return l[0]

print(find_max([1, 4, 45, 6, -50, 10, 2]))
print(find_max([1, 4, 45, 6, 70, 10, 82]))
# => 45