'''

'''
class Node(object):
    edgelist = []
    attr_list = {}
    """
    attr_list:
        - id : the node's ID
    """ 
    def __init__(self, _edgelist, _attr_list = None):
        self.edgelist = _edgelist
        self.attr_list = _attr_list
    
    def degree(self):
        return len(self.edgelist)
    
    def weighted_degree(self):
        return sum([edge.attr_list['weight'] for edge in self.edgelist])
        
    def get_node(self):
        return {'edgelist' : self.edgelist.copy(), 'attr list': self.attr_list.copy()}
    
    def get_attrlist(self):
        return self.attr_list
    
    def set_attr_list(self, attr_list_):
        self.attr_list=attr_list_