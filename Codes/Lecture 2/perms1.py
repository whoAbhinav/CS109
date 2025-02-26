# How many letter orderings are possible for the string ;boba'?

import itertools

def main():
    letters = ['b','o','b','a']
    perms = set(itertools.permutations(letters))
    for perm in perms:
        pretty_perm = "".join(perm)
        print(pretty_perm)

if __name__ == "__main__":
    main()