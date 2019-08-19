from os.path import split
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(split(__file__)[1],__name__,str(__package__)))


import mydata.modelclass
from mydata.modelclass import ModelClass
from mydata.anotherclass import AnotherClass
import processed
import processed.util
import configdata
#import mydata

#print(ModelClass)

#print(mydata.get_data())

#print(mydata.modelclass.ModelClass(), mydata.modelclass.ModelClass)
import pickle
with open('mydata/df/myfile.pic','rb') as f:
    m = pickle.load(f)
    print(m)

