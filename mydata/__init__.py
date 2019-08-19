import pickle

from .modelclass import ModelClass
from .anotherclass import AnotherClass

foldname = 'mydata/'

def get_data(prefix='./'):
    dffname = '{}/{}/df/myfile.pic'.format(prefix,foldname,)
    with open(dffname,'rb') as f:
        df = pickle.load(f)
    return df

