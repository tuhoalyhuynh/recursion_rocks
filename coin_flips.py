# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    # Write code here
    if type(n) != int:
        raise TypeError('Value must be an integer')
    if n < 1:
        raise ValueError('Must be greater than zero')

    # Base case
    if n == 1:
        results = ['H', 'T']
        return results
    else:
        possible_results = ['H', 'T']
        results = []
        for i in possible_results:
            for result in coin_flips(n -1):
                results.append(i + result)
        return results


print(coin_flips(2)) 
# => ["HH", "HT", "TH", "TT"]