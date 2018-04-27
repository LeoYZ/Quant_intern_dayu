
# coding: utf-8

# In[2]:


def alpha132(dv, param=None):
    default_param = {'t': 20}
    if not param:
        param = default_param
        
    dv.add_field('turnover',ds)
    alpha132 = dv.add_formula('alpha132',"Ts_Mean(turnover,t)".format(param['t']),is_quarterly=False)
    
    return alpha132

