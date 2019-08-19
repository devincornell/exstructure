from os.path import split
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(split(__file__)[1],__name__,str(__package__)))

# TO BE ACCESSED USING RELATIVE IMPORT
class AnotherClass:
    def __init__(self,d=12):
        self.ha = None
    def get(self):
        return self.ha

