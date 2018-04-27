
# coding: utf-8

# In[1]:


import  pandas as pd


# In[2]:


def get_dv(start = 20170101, end = 20180101):
    import jaqs_fxdayu
    jaqs_fxdayu.patch_all()
    from jaqs.data import DataView
    from jaqs_fxdayu.data.dataservice import LocalDataService
    
    import warnings
    warnings.filterwarnings("ignore")
    
    factor_list = ['alpha13','alpha39', 'alpha109', 'alpha131', 'alpha132', 'alpha169', 'EquityTRate', 'PCF',
                  'turnover', 'oper_rev', 'tot_assets', 'total_liab', 'capital_stk', 'ncf_oper_ttm']
    check_factor = ','.join(factor_list)
    
    dataview_folder = r'E:\Quant\fxdayu\Git\data'
    ds = LocalDataService(fp = dataview_folder)
    
    ZZ800_id = ds.query_index_member('000906.SH', start, end)
    stock_symbol = list(set(ZZ800_id))
    
    dv_props = {'start_date': start, 'end_date': end, 'symbol':','.join(stock_symbol),
                'fields': check_factor,
                 'freq': 1,
                 'prepare_fields': True}
    
    dv = DataView()
    dv.init_from_config(dv_props, data_api=ds)
    dv.prepare_data()
    return dv

if 'dv' not in dir():
    dv = get_dv()


# In[3]:


def test(factor, data):
    if not isinstance(data, pd.core.frame.DataFrame):
        raise TypeError('On factor {}, output must be a pandas.DataFrame!'.format(factor))
    else:
        try:
            index_name = data.index.names[0]
            columns_name = data.columns.names[0]  
        except:
            if not (index_name in ['trade_date', 'report_date'] and columns_name == 'symbol'):
                raise NameError('''Error index name, index name must in ["trade_date", "report_date"], columns name must be "symbol"''')
                
        index_dtype = data.index.dtype_str
        columns_dtype = data.columns.dtype_str
         
        if columns_dtype not in ['object', 'str']:
            raise TypeError('error columns type')
        
        if index_dtype not in ['int32','int64','int']:
            raise TypeError('error index type')
        
        print ('{} OK!'.format(factor))


# In[4]:


from alpha13 import alpha13

test('alpha13',globals()['alpha13'](dv))


# In[5]:


from alpha39 import alpha39

test('alpha39',globals()['alpha39'](dv))


# In[6]:


from alpha109 import alpha109

test('alpha109',globals()['alpha109'](dv))


# In[7]:


from alpha131 import alpha131

test('alpha131',globals()['alpha131'](dv))


# In[8]:


from alpha169 import alpha169

test('alpha169',globals()['alpha169'](dv))


# In[9]:


from alpha132 import alpha132

test('alpha132',globals()['alpha132'](dv))


# In[10]:


from EquityTRate import EquityTRate

test('EquityTRate',globals()['EquityTRate'](dv))


# In[11]:


from PCF import PCF

test('PCF',globals()['PCF'](dv))

