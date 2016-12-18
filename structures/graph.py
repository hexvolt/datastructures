from collections import Sized, Hashable, Iterable, Container


class Vertex(object):
    """
    Represent a Vertex of a Graph. Each Vertex has a name and may be connected
    to unlimited amount of other Vertices.
    """

    name = None
    
    def __init__(self, name):
        super(Vertex, self).__init__()
        
        if not isinstance(name, Hashable):
            raise TypeError('Vertex name should be string or integer value.')        

        self.name = name
        self.connections = {}
    
    def connect_to(self, vertex, weight=None, bidirectional=False):
        self.connections[vertex.name] = weight
        
        if bidirectional:
            vertex.connections[self.name] = weight
    
    def __repr__(self):
        return "Vertex({})".format(self.name)


class Graph(Sized, Iterable, Container):
    """
    Represents a Graph data structure which comprises a set of Vertices.
    May be directed (the connection between Vertices matters) or undirected.
    """
    
    def __init__(self, undirected=True):
        self.vertices = {}
        self._undirected = undirected
        
    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices[name] = vertex

        return vertex
    
    def add_edge(self, name_a, name_b, weight=None):
        if name_a == name_b:
            raise ValueError()
        
        vertex_a = self.vertices.get(name_a) or self.add_vertex(name_a)
        vertex_b = self.vertices.get(name_b) or self.add_vertex(name_b)
        
        vertex_a.connect_to(vertex_b, weight, self._undirected)
    
    def find_path(self, name_a, name_b):
        pass
    
    def dfs_paths(self, current_vertex, end_vertex, path=[]):
        path += [current_vertex]
        
        if current_vertex == end_vertex:
            yield path
        
        for adjacent_name in current_vertex.connections.keys():
            adjacent = self.vertices[adjacent_name]
            
            if adjacent in path:
                continue    # no turning back
            
            for p in self.dfs_paths(adjacent, end_vertex, path):
                yield p
    
    def lowest_weight(self, name_a, name_b):
        pass
    
    def shortest_way(self, name_a, name_b):
        pass
    
    def __iter__(self):

        for name, vertex in self.vertices.iteritems():
            yield vertex
    
    def __contains__(self, name):
        return name in self.vertices
    
    def __len__(self):
        return len(self.vertices)
    
    def __repr__(self):
        vertices = ', '.join(map(str, self))
        return "Graph({})".format(vertices)


if __name__ == '__main__':
    g = Graph(undirected=True)

    g.add_edge('Lviv', 'Kiev', 540)
    g.add_edge('Lviv', 'Odessa', 600)
    g.add_edge('Kiev', 'Odessa', 700)
    g.add_edge('Kiev', 'Town', 100)
    g.add_edge('Town', 'Odessa', 200)
    g.add_edge('Lviv', 'A', 200)
    g.add_edge('Kiev', 'B', 200)
    g.add_edge('B', 'C', 200)

    g.dfs_paths(g.vertices['C'], g.vertices['A'])
