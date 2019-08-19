# PRINT OUT CURRENT FILE INFO
from os.path import split
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(split(__file__)[1],__name__,str(__package__)))

# START WITHIN PACKAGE DATA
import sys
sys.path.append('..')
#import files in folders above
from mydata.modelclass import ModelClass
from processed.util import utilfunc
# import file in folder above
from configdata import configdat

print(configdat)

print(utilfunc)
m = ModelClass(20)

import pickle
with open('df/myfile.pic','wb') as f:
    pickle.dump(m, f)

