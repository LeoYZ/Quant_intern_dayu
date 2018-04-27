
# coding: utf-8

# In[1]:


def alpha131(dv, param=None):
    default_param = {'t1':50, 't2':18, 't3':18}
    if not param:
        param = default_param
        
    alpha131 = dv.add_formula('alpha131',"(Rank(Delta(vwap, 1))^Ts_Rank(Correlation(close,Ts_Mean(volume,t1), t2), t3))"
                         .format(param['t1'],param['t2'],param['t3']) ,is_quarterly=False)
    
    return alpha131

