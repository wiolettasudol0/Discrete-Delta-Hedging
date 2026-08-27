# Discrete Delta-Hedging & Tracking Error in the Black-Scholes Model

## Overview
In continuous-time Black-Scholes financial market models, a self-financing portfolio perfectly replicates a European Call option ($V_{x,y}(T) = (S(T) - K)^+$). However, in realistic market environments, portfolios can only be rebalanced at discrete time intervals $t_i = i \frac{T}{m}$, which inevitably induces **tracking / hedging error** ($X$):

$$X := V_{x,y}(t_m) - (S(t_m) - K)^+$$

This project simulates dynamic delta-hedging strategies via Monte Carlo paths ($N=2000$) to evaluate:
1. **Convergence & Accuracy:** Tracking error expectation $\mathbb{E}[X]$ and volatility $\sigma_X = \sqrt{\text{Var}(X)}$ as the rebalancing frequency increases ($m \in \{5, 10, 20, 40, 80\}$).
2. **Proportional Transaction Costs:** Portfolio friction and hedging degradation under proportional costs $|x(t_i) - x(t_{i-1})| \delta S(t_i)$ (e.g., $\delta = 0.01$).
3. **Event-Driven / Threshold Rebalancing:** Adaptive rebalancing strategies triggered only when relative asset price fluctuations exceed a threshold:
$$\frac{|S(t_i) - S(t_{i-1})|}{S(t_{i-1})} > \varepsilon \quad (\varepsilon = 0.05 ) $$ 

---


## Project Structure
* BSModel.py     
* Pricers.py     
* Hedging.py      
* main.py        
