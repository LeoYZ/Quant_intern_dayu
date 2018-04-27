
# coding: utf-8

# In[1]:


def alpha13(dv,param=None):
    alpha13 = dv.add_formula('alpha13',"(high*low)^0.5-vwap"
                        , is_quarterly=False)
    return alpha13

