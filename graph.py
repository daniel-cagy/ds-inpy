
from collections import deque

class Graph:
    def __init__(self, num_vertices: int, edges: list[tuple[int, int]]) -> None:
        self.mtx: list[list[int | None]] = [
            [None] * num_vertices for _ in range(num_vertices)
        ]
        for edge in edges:
            i, j = edge
            self.mtx[i][j] = True
            self.mtx[j][i] = True

    def dfs(self, start: int, target: int) -> bool:
        seen = [False for _ in range(len(self.mtx))]
        to_be_seen = deque()
        to_be_seen.append(start)
        seen[start] = True
        while to_be_seen:
            current = to_be_seen.pop()
            if current == target:
                return True
            adjacency = self.mtx[current]
            for i in range(len(adjacency)):
                has_edge = adjacency[i]
                if has_edge and not seen[i]:
                    seen[i] = True
                    to_be_seen.append(i)
        return False

    def bfs(self, start: int, target: int) -> bool:
        seen = [False for _ in range(len(self.mtx))]
        to_be_seen = deque()
        to_be_seen.append(start)
        seen[start] = True
        while to_be_seen:
            current = to_be_seen.popleft()
            if current == target:
                return True
            adjacency = self.mtx[current]
            for i in range(len(adjacency)):
                has_edge = adjacency[i]
                if has_edge and not seen[i]:
                    seen[i] = True
                    to_be_seen.append(i)
        return False


if __name__ == "__main__":
    g = Graph(6, [(0, 1), (1, 2), (0, 3), (2, 4)])

    print(g.dfs(0, 4))  # True
    print(g.dfs(0, 5))  # False
    print(g.dfs(0, 3))  # True
    print(g.dfs(5, 5))  # True

    print(g.bfs(0, 4))  # True
    print(g.bfs(0, 5))  # False
    print(g.bfs(0, 3))  # True
    print(g.bfs(5, 5))  # True



