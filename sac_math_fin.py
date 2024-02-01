def find_amortization(total, parts):
    return total/parts

def find_interest(total, tax):
    return total * (tax / 100)

def find_installment_one(interest, amortization):
    return interest + amortization

def find_constant(amortization, tax):
    return amortization * (tax / 100)

def find_installment_n(installment_one, cons, n):
    return installment_one - ((n - 1) * cons)


def A(T, N):
    return T/N
def J1(T, i):
    return T * i
def P1(A, J1):
    return A + J1
def k(A, i):
    return A * i
def Pn(P1, k, n):
    return P1 - ((n - 1) * k)

T = 200
N = 4
i = 10
th = 3
amor = find_amortization(T, N)
inter = find_interest(T, i)
installment = find_installment_one(inter, amor)
cons = find_constant(amor, i)

print(f"A = {amor}, J1 = {inter}, P1 = {installment}, k = {cons}")
print(f"{th}th = {find_installment_n(installment, cons, th)}")