from os.path import join as _join, dirname as _dirname
from os.path import abspath as _abspath 
import pandas as _pandas

datadir = _abspath( _join(_dirname(__file__), '..', 'ohmyyeast-data') ) 

def load_optpub():
    _cols = ['AID','e2','e3','e4','e5','e6','e7','e8','e9', 'e10', 'S','k_SA','K_SA',
            'k_BA','K_BA','ki_BA', 'Ki_BA','k_CA','K_CA','ki_CA', 'Ki_CA','k_AA',
            'K_AA','ki_AA','Ki_AA','k_AB','K_AB','ki_AB', 'Ki_AB', 'k_CB','K_CB','ki_CB',
            'Ki_CB','k_BB', 'K_BB','ki_BB','Ki_BB','k_BC','K_BC', 'ki_BC', 'Ki_BC','k_AC',
            'K_AC','ki_AC','Ki_AC','k_CC', 'K_CC','ki_CC','Ki_CC', 'ki_EA',
            'Ki_EA','ki_EB', 'Ki_EB','ki_EC','Ki_EC','k_FA','K_FA','k_FB', 'K_FB','k_FC',
            'K_FC','FUS1MAX','Ke50_FUS1','kd', 'ks','n','At','Bt','Ct','E','F', 'fVal']

    myfile = _join(datadir, 'opt/pub', 'reduced.mat.csv') 
    dataset = _pandas.read_csv(myfile, names=_cols) 

    for edge in ['e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10']: 
        dataset[edge] = dataset[edge].astype(int) 

    return dataset 

def load_optsnu():
    myfile = _join(datadir, 'opt/snu', 'reduced.mat.csv') 
    dataset = _pandas.read_csv(myfile) 
    for edge in ['e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10']: 
        dataset[edge] = dataset[edge].astype(int) 

    return dataset 

def test_this():
    from ohmyyeast import datasets 

    pub = datasets.load_optpub() 

    snu = datasets.load_optsnu() 


    import ipdb; ipdb.set_trace()

     
