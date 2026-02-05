class Nodes:
    def __init__(self, city, parent=None, g=0):
        self.city = city
        self.parent = parent
        self.g = g

    def path(self):
        node, p = self, []
        while node:
            p.append(node.city)
            node = node.parent
        return list(reversed(p))