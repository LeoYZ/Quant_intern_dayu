
# coding: utf-8

# In[1]:


def EquityTRate(dv,param=None):

    EquityTRate = dv.add_formula('EquityTRate_J','oper_rev/(tot_assets-total_liab)',
                                is_quarterly=False)
    
    return EquityTRate

