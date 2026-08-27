import numpy as np
from BSModel import DeltaEurCall, PriceEurCall
from Pricers import NormalSample


def DeltaHedgingError(model, T, K, m, N, delt, eps):

    # parametry modelu
    r = model.r
    mu = model.mu
    sigma = model.sigma
    S0 = model.S0

    X = np.zeros(N)
    dt = T / m # długość kroku czasowego

    for n in range(N):

        Z = NormalSample(m)
        S = np.zeros(m + 1)
        S[0] = S0

        for i in range(1, m + 1):
            S[i] = S[i-1]*np.exp((r - 0.5 * sigma**2)*dt+sigma*np.sqrt(dt) * Z[i-1])

        x = DeltaEurCall(S[0], r, sigma, T, K)
        y = PriceEurCall(S[0], r, sigma, T, K) - x * S[0] # y(0)=u(0,S(0))-x(0)S(0)


        for i in range(1, m + 1):

            tau = T - i * dt   # czas do wygaśnięcia

            # ==== Pytanie 3 ====
            if eps == 0:
                reb = True # przypadek z pytania 1 i 2
            else:
                price_change = abs(S[i]-S[i-1])/S[i-1] # sprawdzamy zmianę ceny
                if price_change > eps:
                    reb = True
                else:
                    reb = False

            if tau > 0 and reb == True:
                x_new = DeltaEurCall(S[i], r, sigma, tau, K) # x(t_i)
            else:
                x_new = x

            # ==== Pytanie 2 ====
            if delt > 0:
                cost = abs(x-x_new)*delt*S[i]
            else:
                cost=0.0

            y = y * np.exp(r*dt) + (x - x_new) * S[i] - cost # y(t_i)=y(t_{i−1})A(t_i)+[x(t_{i-1})−x(t_i)]*S(t_i).
            x = x_new # x(t_i)

        V_T = x * S[m] + y* np.exp(r*dt) # V(t)=x(t)*S(t)+y(t)*A(t)
        payoff = max(S[m] - K, 0.0)
        X[n] = V_T - payoff # X=V(t)-(S(t)-K)^+

    EX = np.mean(X)
    stdX = np.std(X, ddof=1)

    return EX, stdX
