from os.path import join as _join 
import pandas as _pandas 

datadir = '/root/share/data'

def reduced():
    file = _join(datadir, 'reduced.mat.csv')
    df0 = _pandas.read_csv(file)
    # import ipdb; ipdb.set_trace()
    df0.e2 = df0.e2.astype(int)
    df0.e3 = df0.e3.astype(int)
    df0.e4 = df0.e4.astype(int)
    df0.e5 = df0.e5.astype(int)
    df0.e6 = df0.e6.astype(int)
    df0.e7 = df0.e7.astype(int)
    df0.e8 = df0.e8.astype(int)
    df0.e9 = df0.e9.astype(int)    
    df0.e10 = df0.e10.astype(int)        
    return df0 

def reduced_avg(): 
    file = _join(datadir, 'reduced_avg.mat.csv')
    df0 = _pandas.read_csv(file)
    df0.e2 = df0.e2.astype(int)
    df0.e3 = df0.e3.astype(int)
    df0.e4 = df0.e4.astype(int)
    df0.e5 = df0.e5.astype(int)
    df0.e6 = df0.e6.astype(int)
    df0.e7 = df0.e7.astype(int)
    df0.e8 = df0.e8.astype(int)
    df0.e9 = df0.e9.astype(int)    
    df0.e10 = df0.e10.astype(int)
    return df0 

def test_reduced(): 
    data1 = reduced() 
    data2 = reduced_avg()
    import ipdb; ipdb.set_trace() 
