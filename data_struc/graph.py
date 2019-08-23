class Node(object):
    def __init__(self,value):
        self.value = value
        self.edges = []

class  Edge(object):
    def __init__(self, value, node_from,node_to):
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes = [], edges =[] ):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self,new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self,new_edge_val,node_from_val,node_to_val):
        from_bound  = None
        to_bound = None
        for node in self.nodes:
                if node_from_val == node.value:
                    from_bound = node
                if node_to_val == node.value:
                    to_bound = node
        if from_bound == None:
            from_bound = Node(node_from_val)
            self.nodes.append(from_bound)
        if to_bound == None:
            to_bound = Node(node_from_val)
            self.nodes.append(to_bound)
        new_edge = Edge(new_edge_val,from_bound,to_bound)
        from_bound.edges.append(new_edge)
        to_bound.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        edge_list = []
        for edge_object in self.edges:
            edge = (edge_object.value,edge_object.node_from.value,edge_object.node_to.val)
            edge_list.append(edge)

    def get_max_index(self):
        max_index   = -1
        if(len(self.nodes)):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index


    def get_adjacency_list(self):
        max_index = self.get_max_index()
        adjacency_list = [None]*(max_index + 1)
        for edge_object in self.edges:
            if(adjacency_list[edge_object.node_from.val]):
                adjacency_list[edge_object.node_from.val].append(edge_object.node_to.value, edge_object.value)
            if(adjacency_list[edge_object.node_to.val]):
                adjacency_list[edge_object.node_to.val]=[(edge_object.node_to.value, edge_object.value)]

        return adjacency_list 

    def get_adjacency_martix(self):
        max_index= self.get_max_index()
        adjacency_martix = [[0 for i in range(max_index+1)]for j in range(max_index+1)]
        for edge_object in self.edges:
            adjacency_martix[edge_object.node_from.val][edge_object.node_to.val] = edge_object.val
        return adjacency_martix
