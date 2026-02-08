class Nodes:
    # Initialize node with city, optional parent, and cumulative cost g
    def __init__(self, city, parent=None, g=0):
        self.city = city
        self.parent = parent
        self.g = g

    # Return the path from start node to this node as a list of city names
    def path(self):
        node, p = self, []
        while node:
            p.append(node.city)
            node = node.parent
        return list(reversed(p))