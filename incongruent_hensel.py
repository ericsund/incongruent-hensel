import sympy as sp
import numpy as np

modulus = 144
# f = x^5 + x - 6
x = sp.symbols('x')
f = x**5 + x - 6
congruence = 0

"""
x^5 + x - 6 congruent (0 mod 144)
"""

# first, factor the modulus into a product of primes
prime_factors = []
if not sp.isprime(modulus):
    p = sp.factorint(144)
    for i in p:
        prime_factors.append([i, p[i]])

    print(prime_factors)

def solve_subproblem(level_base):
    # f(x) congruent 0 mod (2) ?
    sols = []
    for i in range(level_base):
        # if np.polyval([1, 0, 0, 0, 1, -6], i) % level_base == congruence:
        if f.replace(x, i) % level_base == congruence:
            sols.append(i)
    
    # now, for all the sols... (0, 1)
    count = 0
    i = 0
    while i < len(sols):
    # for i in range(len(sols)):
        print("count: " + str(count))
        print("sols: " + str(sols))
        f_prime = sp.diff(f)
        
        # f'(0) congruent (0 mod 2) ?
        if f_prime.replace(x, sols[i]) % level_base == congruence:

            # stop once we've reach the biggest congruence class
            if level_base**(count+1) > 16:
                print(sols)
                break
            # f'(1) congruent 0 (mod 2) AND f(1) congruent 0 (mod 4) ?
            print("sols[i]: " + str(sols[i]))
            print("modder: " + str(level_base**(count+1)))
            print("here: " + str( f.replace(x, sols[i]) % level_base**(count+1)))
            if f.replace(x, sols[i]) % level_base**(count+1) == congruence:
                
                # lifts to solutions in larger congruence classes
                # find these congruence classes...
                r = sols[i]
                sols = []
                t = 0
                print("i: " + str(i))
                print(sols)
                while r + (t*(level_base**(count))) % level_base**(count+1) < level_base**(count+1):
                    print("so far we have: " + str(r + (t*(level_base**(count))) % level_base**(count+1)))
                    sols.append(r + (t*(level_base**(count))))
                    t += 1
                    if r + (t*(level_base**(count))) > level_base**(count+1):
                        print("lifts to solutions mod " + str(level_base**(count+1)) + " and they are " + str(sols))
                        break
                i = 0
                count += 1
                continue
            # f(1) NOT congruent 0 (mod 8) ?
            else:
                # there are no further solutions
                i += 1
                pass

        # f'(0) NOT congruent (0 mod 2) ?
        # lifts to unique solution mod 2^4
        else:
            print("lifts to unique solution mod " + str(9))
            unique_sols[count] += 1
            count += 1
            i += 1

    print("--------------------")
    print("unique_sols " + str(unique_sols))
    print("sols " + str(sols))
    print("number of unique solutions mod 16: " + str(len(unique_sols) * len(sols)))

# solve each subproblem (n prime factors == n subproblems)
# the # of unique solutions in each prime factor^k, in order they're presented in prime_factors
unique_sols = [0]*len(prime_factors)
for prime_factor in prime_factors:
    print("\n\nSOLVING SUBPROBLEM WITH " + str(prime_factor[0]))
    solve_subproblem(prime_factor[0])
    

