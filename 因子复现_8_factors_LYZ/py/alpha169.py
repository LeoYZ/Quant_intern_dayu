
# coding: utf-8

# In[1]:


def alpha169(dv,param=None):

    def SMA(A,n,m):
        alpha = m/n
        return A.ewm(alpha=alpha, adjust=False).mean()
    
    default_param = {'t1':12, 't2':26, 't3': 10, 't4':1}
    if not default_param:
        param = default_param
    
    alpha169 = dv.add_formula('alpha169',"SMA(Ts_Mean(Delay(SMA(close-Delay(close,1),9,1),1),{}) - Ts_Mean(Delay(SMA(close-Delay(close,1),9,1),1),{}),{},{})"
                              .format(param['t1'], param['t2'], param['t3'], param['t4'])
                            ,is_quarterly=False, register_funcs={"SMA":SMA})
    
    return alpha169

