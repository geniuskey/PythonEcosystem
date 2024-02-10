from pyvis.network import Network

# 네트워크 객체 생성
net = Network(notebook=True)

# 노드 추가
net.add_node(1, label='Node 1')
net.add_node(2, label='Node 2')

# 엣지 추가
net.add_edge(1, 2)

# 네트워크 시각화
net.show('mygraph.html')
