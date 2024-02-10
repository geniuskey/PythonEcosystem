import os
import webbrowser
from pyvis.network import Network
import networkx as nx

nt = Network(notebook=True)
nt.from_nx(nx.davis_southern_women_graph())
html_path = os.path.abspath('nx.html')
nt.show(html_path)
webbrowser.open('file://' + html_path)
