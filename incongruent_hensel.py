import sympy as sp
import numpy as np

modulus = 144
# f = x^5 + x - 6
x = sp.symbols('x')
f = x**5 + x - 6
f_prime = sp.diff(f)
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

def solve_subproblem(p, count):
    # f(x) congruent 0 mod (2) ?
    sols = []
    for i in range(p):
        # if np.polyval([1, 0, 0, 0, 1, -6], i) % p == congruence:
        if f.replace(x, i) % p == congruence:
            sols.append(i)
    print("Trivial solutions to " + str(f) + " mod " + str(p) + ":")
    print("\t => x = " + str(sols))
    
    # now, test all the sols... (0, 1)
    i = 0
    level = 2
    while i < len(sols):
        # we don't want to exceed our maximum congruence
        if p**level > (prime_factors[count][0] ** prime_factors[count][1]):
            break

        # f'(0) congruent (0 mod 2) ?
        if f_prime.replace(x, sols[i]) % p == congruence:
            print("f'(" + str(sols[i]) + ") mod " + str(p) + " = " + str(f_prime.replace(x, sols[i]) % p))
            # stop once we've reach the biggest congruence class
            if p**(count+1) > 16:
                print(sols)
                break
            # f'(1) congruent 0 (mod 2) AND f(1) congruent 0 (mod 4) ?
            if f.replace(x, sols[i]) % p**(level) == congruence:
                print("f(" + str(sols[i]) + ") mod " + str(p**level) + " = " + str(f.replace(x, sols[i]) % p**level))
                # lifts to solutions in larger congruence classes
                # find these congruence classes...
                r = sols[i]
                sols = []
                t = 0
                while r + (t*(p**(count))) % p**(count+1) < p**(level):
                    # print("so far we have: " + str(r) + " + " + str(t) + "*" + str(p) + "^" + str(level-1) + " = " + str(r + (t*(p**(level-1)))))
                    sols.append(r + (t*(p**(level-1))))
                    t += 1
                    if r + (t*(p**(level-1))) > p**(level):
                        print("\t => lifts to further solutions mod " + str(p**(level)) + " and they are: " + str(sols))
                        break
                level += 1
                i = 0
                continue
            # f(1) NOT congruent 0 (mod 8) ?
            else:
                print("f(" + str(sols[i]) + ") mod " + str(p**level) + " = " + str(f.replace(x, sols[i]) % (p**level)))
                print("\t => no further solutions")
                # there are no further solutions
                i += 1
                pass

        # f'(0) NOT congruent (0 mod 2) ?
        # lifts to unique solution mod 2^4
        else:
            print("f'(" + str(sols[i]) + ") mod " + str(p) + " = " + str(f_prime.replace(x, sols[i]) % p) + " != " + str(congruence))
            print("\t => lifts to a unique solution mod " + str(prime_factors[count][0] ** prime_factors[count][1]))
            unique_sols[count] += 1
            i += 1

    print("===> subproblem on " + str(prime_factor[0]) + " prime complete!")
    
    # display the solutions in the congruence class
    # note: sols has the trivial solutions initially, and is replaced with further solutions in higher congruences
    # if we never get any futher solutions, don't count sols
    if p**(level-1) < prime_factors[count][0] ** prime_factors[count][1]:
        solutions_congruences.append(unique_sols[count])
        print("number of solutions mod " + str(prime_factors[count][0] ** prime_factors[count][1]) + ": " + str(unique_sols[count]))
    else:
        solutions_congruences.append(unique_sols[count] + len(sols))
        print("number of solutions mod " + str(prime_factors[count][0] ** prime_factors[count][1]) + ": " + str(unique_sols[count] + len(sols)))
    
    count += 1
    return [count, solutions_congruences]

# solve each subproblem (n prime factors == n subproblems)
# the # of unique solutions in each prime factor^k, in order they're presented in prime_factors
unique_sols = [0]*len(prime_factors)
count = 0
solutions_congruences = []
for prime_factor in prime_factors:
    print("\n\nSOLVING SUBPROBLEM WITH " + str(prime_factor[0]))
    [count, solutions_congruences] = solve_subproblem(prime_factor[0], count)

# display the final number of solutions
final = 1
for i in solutions_congruences:
    final *= i
print("==========================================")
print("total number of solutions: " + str(final))