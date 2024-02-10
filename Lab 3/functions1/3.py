#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
a, b = 35, 94
def solve(numheads, numlegs):
    for chikens in range(numheads):
        rabbits = numheads - chikens
        if (2*rabbits + 4*chikens) == numlegs:
            return rabbits, chikens
    return "NON"
print(solve(a, b))
