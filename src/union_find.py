
class UnionFind:
    def __init__(self, num_elements: int) -> None:
        self.univ = [i for i in range(num_elements)]

    def find_parent(self, i: int) -> int:
        current = i
        path = []
        while self.univ[current] != current:
            path.append(current)
            current = self.univ[current]
        return current

    def optimize_path(self, path: list, parent: int):
        for element in path:
            self.univ[element] = current

    def union(self, i: int, j: int) -> None:
        k = self.find_parent(i)
        l = self.find_parent(j)



UnionFind(5)
