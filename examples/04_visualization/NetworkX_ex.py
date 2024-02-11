import networkx as nx
import matplotlib.pyplot as plt

# 그래프 객체 생성
G = nx.Graph()

# 노드 추가
G.add_node("A")
G.add_node("B")
G.add_node("C")

# 엣지 추가
G.add_edge("A", "B")
G.add_edge("B", "C")

# 최단 경로 계산
print(nx.shortest_path(G, "A", "C"))

# 시각화
pos = {"A": (0, 0), "B": (0.5, 0.5), "C": (1, 0)}
options = {
    "font_size": 30,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)
plt.gca().margins(0.3)
plt.axis("off")
plt.show()
