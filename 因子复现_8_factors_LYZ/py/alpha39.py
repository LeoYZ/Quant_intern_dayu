
# coding: utf-8

# In[ ]:


def alpha39(dv,param = None):
    default_param = { 't1':180, 't2':37, 't3':14}
    if not param:
        param = default_param
        
    alpha39 = dv.add_formula('alpha39',
                        "((Rank(Decay_linear(Delta((close), 2),8)) - Rank(Decay_linear(Correlation(((vwap * 0.3) + (open * 0.7)),Ts_Sum(Ts_Mean(volume,{}), {}), {}), 12))) * -1)"
                             .format(param['t1'],param['t2'],param['t3'])
                            ,is_quarterly = False)
    return alpha39

