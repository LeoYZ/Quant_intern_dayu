
# coding: utf-8

# In[1]:


def alpha109(dv,param = None):
    default_param = {'n':10, 'm':2}
    if not param:
        param = default_param
    
    n = param['n']
    m = param['m']
    
    def SMA(A,n,m):
        alpha = m/n
        return A.ewm(alpha=alpha, adjust=False).mean()

    alpha109 = dv.add_formula('alpha109', 
                   "SMA(high-low,{},{})/SMA(SMA(high-low,{},{}),{},{})".format(n,m,n,m,n,m)
                 , is_quarterly=False,
                 register_funcs={"SMA":SMA}
                 )
    
    return alpha109

