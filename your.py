import itertools

words_list = "THEY KNOW YOUR STUPID ALL NASA IS HOAX ASTRONOTS".split()
permutations_list = list(itertools.permutations(words_list))
print("Number of pssible permutations: ", len(permutations_list))
# Uncomment if you have way too much time on your hands
# print(permutations_list)
