'''
This class is for modeling an epidemic spreading.
It defines the hyperedge of the hypegraph in the model.
'''
class Hyperedge(object):
    nodelist = []
    attr_list = []
    
    def __init__(self, _nodelist, _attr_list = None):
        self.nodelist = _nodelist
        self.attr_list = _attr_list
        
    def size(self):
        return len(self.nodelist)
    
    def weighted_size(self):
        return sum([node.attr_list['weight'] for node in self.nodelist])
    
    def print(self):
        print({"nodelist": self.nodelist, "attr list": self.attr_list})
        
    def get_edge(self):
        return {'nodelist' : self.nodelist.copy(), 'attr list': self.attr_list.copy()}
        