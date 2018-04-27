
# coding: utf-8

# In[ ]:


def PCF(dv,param=None):
    
    PCF = dv.add_formula('PCF_J','capital_stk/ncf_oper_ttm',
                    is_quarterly=False)
    
    return PCF

