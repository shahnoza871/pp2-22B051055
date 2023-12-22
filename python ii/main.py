import numpy as np
from endterm import *
# Maximum of the indeces => the max of powers
def max(rr):
    rr = np.array(rr)
    max = 0
    for i in range(rr.shape[0]):
        if rr[i][1] > max:
            max = rr[i][1]
    return max

# gives the result of polynomial 
def polynomial(rr, x):
    x = float(x)
    polynom = np.array(polynom_terms(rr))
    result = 0
    for i in range(polynom.shape[0]):
        c, p = polynom[i]
        result += c*(x**int(p))
    return result
    
# creates a polynomial out of the reccurence relation (rr)
def polynom_terms(rr):
    # terms = [ [coefficient, power] ]
    rr = np.array(rr)
    n = rr.shape[0]
    shape = (n+1, 2)
    terms = np.zeros(shape)
    max_i = max(rr)
    terms[0] = [1, max_i]
    for i in range(n):
        terms[i+1] = [-1*rr[i][0], max_i - rr[i][1]]
    return terms

def derivative(rr, x):
    polynom = np.array(polynom_terms(rr))
    shape = (polynom.shape[0], 2)
    der = np.zeros(shape)
    result = 0
    for i in range(polynom.shape[0]):
        c, p = polynom[i]
        c *= p
        p -= 1
        der[i][0] = c
        der[i][1] = p
    for i in range(der.shape[0]):
        c, p = der[i]
        if p < 0:
            result += 0
        else:
            result += c*(x**p)

    return result

def initial_guess(rr):
    a = 0
    b = 0
    sign = polynomial(rr, a)*polynomial(rr, b)
    n = 0
    while sign > 0:
        a += 1
        b -= 1
        sign = polynomial(rr, a)*polynomial(rr, b)
        n += 1
        if n == 10:
            return 'Error. Couldn\'t find a suiatable initial guess.'
    return (a+b)/2

def solve(rr):
    # Using Newton-Raphson Method
    x = initial_guess(rr)
    # print(f'Initial guess is {x}')
    h = 0.01
    error = polynomial(rr, x)
    max_iteration = 100
    while error > h:
        if max_iteration == 0:
            break
        d = derivative(rr, x)
        if d == 0:
            break
        else:
            x -= polynomial(rr, x)/d
        max_iteration -= 1
    x = round(x, 3)
    return x

def linear(polynom_terms):
    polynom_terms = np.array(polynom_terms)
    return (polynom_terms[1][0]/polynom_terms[0][0])*(-1)

def homogeneous_RR(rr): 
    rr = np.array(rr)
    n = rr.shape[0]
    # n = int(input("Number of terms of the recurrence relation: "))
    # shape = (n, 2)
    # rr = np.zeros(shape)
    # rr = array of [coefficient, index] for each element
    # for i in range(n):
    #     c = float(input(f"Enter the coefficient of {i+1} term: "))
    #     index = int(input(f"Enter the index of {i+1} term is n - "))
    #     rr[i][0] = c
    #     rr[i][1] = index
    # print(rr)
    # print(polynom_terms(rr))
    if n > 1:
        root = solve(rr)
    else:
        root = linear(polynom_terms(rr))
    terms = []
    for i in range(n):
        # makes index
        subscripts = str.maketrans("0123456789n", "₀₁₂₃₄₅₆₇₈₉ₙ")
        # makes power
        superscripts = str.maketrans("0123456789n", "⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ")
        # root is always in power 'n'
        power = 'n'.translate(superscripts)
        # index of the constant
        ind = f'{i+1}'.translate(subscripts)
        # 
        if i == 0:
            terms.append(f'c{ind}({root}){power}')
        # 
        elif i == 1:
            terms.append(f'c{ind}n({root}){power}')
        #
        else:
            p = f'{i}'.translate(superscripts)
            terms.append(f'c{ind}n{p}({root}){power}')
    result = ' + '.join(terms)
    sub_n = 'n'.translate(subscripts)
    return f" a{sub_n} = {result}"

        
def exact_solution(rr, initial_value_entries):
    shape = np.array(rr).shape
    rr = np.zeros(shape)
    rr += np.array(rr)
    n = rr.shape[0]
    initial_values = initial_value_entries
    # n = int(input("Number of terms of the recurrence relation: "))
    # shape = (n, 2)
    # rr = np.zeros(shape)
    # for i in range(n):
    #     c = float(input(f"Enter the coefficient of {i+1} term: "))
    #     index = int(input(f"Enter the index of {i+1} term is n - "))
    #     rr[i][0] = c
    #     rr[i][1] = index
    # initial_values = []
    # for i in range(n):
    #     item = input(f'Enter value of item {i}: ')
    #     initial_values.append(item)

    if n > 1:
        root = solve(rr)
    else:
        root = linear(polynom_terms(rr))
    matrix = np.zeros((n, n))
    for i in range(n):
        if i == 0:
            matrix[i][0] += 1
        if i == 1:
            matrix[i] += root
        if i >= 1:
            for j in range(n):
                matrix[i][j] = (i**j)*(root**i)
    last_column = np.array(initial_values).reshape(n, 1)
    augmented_matrix = np.hstack((matrix, last_column))
    augmented_matrix = Matrix(augmented_matrix)
    coeffs = augmented_matrix.SLE_solution()

    terms = []
    for i in range(n):
        # makes index
        subscripts = str.maketrans("0123456789n", "₀₁₂₃₄₅₆₇₈₉ₙ")
        # makes power
        superscripts = str.maketrans("0123456789n", "⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ")
        # root is always in power 'n'
        power = 'n'.translate(superscripts)
        # index of the constant
        ind = f'{i+1}'.translate(subscripts)
        # 
        if i == 0:
            terms.append(f'{coeffs[i]}({root}){power}')
        # 
        elif i == 1:
            terms.append(f'({coeffs[i]})n({root}){power}')
        #
        else:
            p = f'{i}'.translate(superscripts)
            terms.append(f'({coeffs[i]})n{p}({root}){power}')
    result = ' + '.join(terms)
    sub_n = 'n'.translate(subscripts)
    return f" a{sub_n} = {result}"


class Binary:
    def __init__(self, number):
        self.num = number
    
    def to_decimal(self):
        decimal = 0
        p = 0
        for x in reversed(self.num): # change reversed into a longer expression
            if x == '1':
                decimal += 2**p
            p += 1

        return decimal

    def to_octal(self):
        octal = ""
        decimal = self.to_decimal()
        while decimal > 0:
            remainder = str(decimal%8)
            octal += remainder
            decimal //= 8
        return octal

    def sum(self, other):
        length = max(len(self.num), len(other.num))
        t = 1

        for i in range(length):
            if i < len(self.num):
                s_bit = int(self.num[-i-1])
            else:
                s_bit = 0
            if i < len(other.num):
                o_bit = int(other.num[-i-1])
            else:
                o_bit = 0
            
            result += str((s_bit + o_bit + t)%2)
            t = (s_bit + o_bit + t)//2

            if t != 0:
                result += str(t)
            return Binary(result)


    def product(self, other):
        decimal = self.to_decimal
        result = Binary('0')
        for x in range(decimal):
            result = result.sum(other)
        return result


class Octal:
    def __init__(self, value):
        self.num = value

    def to_decimal(self):
        decimal_value = 0
        octal_str = str(self.num)

        for i in range(len(self.num)):
            decimal_value += int(octal_str[i]) * (8 ** (len(self.num) - i - 1))

        return decimal_value

    def to_binary(self):
        decimal_value = self.to_decimal()
        return bin(decimal_value)[2:]

    def sum(self, other):
        decimal_sum = self.to_decimal() + other.to_decimal()
        return Octal(oct(decimal_sum)[2:])

    def product(self, other):
        decimal_product = self.to_decimal() * other.to_decimal()
        return Octal(oct(decimal_product)[2:])



# print(homogeneous_RR())
# print(exact_solution())