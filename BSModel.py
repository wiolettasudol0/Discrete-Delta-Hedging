import numpy as np
from scipy.stats import norm

class BSModel:
    def __init__(self, S0, r, sigma, mu):
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.mu = mu

def PriceEurCall(S0, r, sigma, T, K):
    d1 = (np.log(S0/K)+(r+0.5*sigma*sigma)*T)/(sigma*np.sqrt(T))
    d2 = (np.log(S0/K)+(r-0.5*sigma*sigma)*T)/(sigma*np.sqrt(T))
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def DeltaEurCall(S0, r, sigma, T, K):
    d1 = (np.log(S0/K)+(r+0.5*sigma*sigma)*T)/(sigma*np.sqrt(T))
    return norm.cdf(d1)
