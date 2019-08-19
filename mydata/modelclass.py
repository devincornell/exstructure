from os.path import split
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(split(__file__)[1],__name__,str(__package__)))

from .anotherclass import AnotherClass

class ModelClass:
    def __init__(self,d=12):
        self.mods = [AnotherClass(d) for _ in range(4)]
    
    def get(self):
        return self.mods
