from BSModel import BSModel
from Hedging import DeltaHedgingError

S0 = 100
r = 0.025
sigma = 0.4
mu=  0.3
T = 0.5
K = 100

model = BSModel(S0, r, sigma, mu)

N = 2000
m_list = [5, 10, 20, 40, 80]

print("m           E(X)           std(X)")
print("___________________________________")

print("Pytanie 1")
for m in m_list:
    wynik = DeltaHedgingError(model, T, K, m, N,0.0,0.0)
    EX = wynik[0]
    stdX = wynik[1]
    print(m, EX, stdX)

print("Pytanie 2")
for m in m_list:
    wynik = DeltaHedgingError(model, T, K, m, N,0.01,0.0)
    EX = wynik[0]
    stdX = wynik[1]
    print(m, EX, stdX)

print("Pytanie 3")
for m in m_list:
    wynik = DeltaHedgingError(model, T, K, m, N,0.01,0.05)
    EX = wynik[0]
    stdX = wynik[1]
    print(m, EX, stdX)