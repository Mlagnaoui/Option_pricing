# -*- coding: utf-8 -*-

import numpy as np
import math
from statistics import mean

def BM(n):
    gauss = np.random.normal(0,math.sqrt(1/n),n)
    gauss = np.insert(gauss,0,0)
    
    return np.cumsum(gauss)

def price(value0,r,sigm,n):
    w = BM(n)
    h = [i*(1/n) for i in range(0,n+1)]
    
    S1 = [sigm*wi for wi in w]
    S2 = [(r-(sigm**2)/2)*hi for hi in h]
    
    S = [value0*math.exp(S1[i]+S2[i]) for i in range(len(S1))]
    
    return S

def call(value0,r,sigm,n,K,t,n_sim):
   
    call_payoff = []    
    trajectory = []
    
    for i in range(n_sim):
        trajectory = price(value0,r,sigm,n)
        call_payoff.append((trajectory[-1]-k)*(trajectory[-1]>=k))
    return math.exp(-r*t)*mean(call_payoff)
        
def put(value0,r,sigm,n,K,t,n_sim):
    
    put_payoff=[]
    trajectory = []
    
    for i in range(n_sim):
        trajectory = price(value0,r,sigm,n)        
        put_payoff.append( (k-trajectory[-1])*(trajectory[-1]<=k) )
    return math.exp(-r*t)*mean(put_payoff)
            
def digital(value0,r,sigm,n,t,n_sim,threshold,payout):
    
    digital_payoff=[]
    trajectory = []
    
    for i in range(n_sim):
        trajectory = price(value0,r,sigm,n)        
        digital_payoff.append(payout*(trajectory[-1]>threshold))
    return math.exp(-r*t)*mean(digital_payoff)
    
def lookback(value0,r,sigm,n,t,n_sim):
    lookback_payoff = []
    trajectory = []
    
    for i in range(n_sim):
        trajectory = price(value0,r,sigm,n)
        lookback_payoff.append(trajectory[-1]-min(trajectory))
    return math.exp(-r*t)*mean(lookback_payoff)

def asian(value0,r,sigm,n,t,n_sim):
    asian_payoff = []
    trajectory = []
    
    for i in range(n_sim):
        trajectory = price(value0,r,sigm,n)
        asian_payoff.append(trajectory[-1]-mean(trajectory))
    return math.exp(-r*t)*mean(asian_payoff)