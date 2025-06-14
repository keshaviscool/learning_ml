
n = int(input())

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# def nCk(n, k):
#     if not isinstance(n, int) or not isinstance(k, int) or n < 0 or k < 0:
#         return 0
#     if k > n:
#         return 0  # Cannot choose more items than available
#     if k == 0 or k == n:
#         return 1
    
#     num = factorial(n)
#     den = factorial(k) * factorial(n - k)
    
#     return num // den  #


def string_permutations(s):
    if len(s) == 1:
        return [s]
    
    permutations = []
    for i in range(len(s)):
        first_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        
        for perm in string_permutations(remaining_chars):
            permutations.append(first_char + perm)
            
    return permutations

for i in range(n):
    n_inp = input().split()

    len_of_string = int(n_inp[0])
    no_of_ones = int(n_inp[1])
    no_of_zeros = len_of_string - no_of_ones

    string_ = ""

    for i in range(no_of_ones):
        string_ += "1"

    for i in range(no_of_zeros):
        string_ += "0"

    permutated_strings = string_permutations(string_)
    found = False
    for perm in permutated_strings:
        if found:
            break

        count_010 = perm.count("010")
        count_101 = perm.count("101")

        # print(count_010, count_101)

        if (count_010 == count_101) and (count_101 != 0):
            found = True
            print(int(perm))
            break

    if not found:
        string__ = ""
        for i in range(len_of_string):
            string__ += "0"

        print(int(string_))


    

    # print("No of possible strings", nCk(len_of_string, no_of_ones))


    



    
   
