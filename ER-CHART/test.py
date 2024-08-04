import pydot
from IPython.display import Image

# 创建一个新的无向图
graph = pydot.Dot(graph_type='graph', dpi=600)

# 定义实体节点
entity_node = pydot.Node("jingdianxinxi", shape="rectangle", style="filled", fillcolor="lightgrey")
graph.add_node(entity_node)

# 定义属性节点
attributes = [
    ("id", "int (PK)", "ellipse", "yellow"),
    ("jingdianbianhao", "varchar(50)", "ellipse", "white"),
    ("jingdianmingcheng", "varchar(255)", "ellipse", "white"),
    ("suoshudiqu", "int (FK)", "ellipse", "lightblue"),
    ("tupian", "text", "ellipse", "white"),
    ("kaifangshijian", "varchar(255)", "ellipse", "white"),
    ("fujinmeishi", "text", "ellipse", "white"),
    ("dizhi", "varchar(255)", "ellipse", "white"),
    ("piaojia", "decimal(18, 2)", "ellipse", "white"),
    ("liulanliang", "int", "ellipse", "white"),
    ("miaoshu", "longtext", "ellipse", "white"),
    ("addtime", "timestamp", "ellipse", "white")
]

# 将属性分成两组，以便围绕实体节点的两侧
top_left_attributes = attributes[:len(attributes)//2]
bottom_right_attributes = attributes[len(attributes)//2:]

# 添加左上方属性节点并连接到实体节点
for attribute, attr_type, shape, fillcolor in top_left_attributes:
    attribute_node = pydot.Node(f"{attribute}: {attr_type}", shape=shape, style="filled", fillcolor=fillcolor)
    graph.add_node(attribute_node)
    graph.add_edge(pydot.Edge(entity_node, attribute_node, dir='none'))

# 添加右下方属性节点并连接到实体节点
for attribute, attr_type, shape, fillcolor in bottom_right_attributes:
    attribute_node = pydot.Node(f"{attribute}: {attr_type}", shape=shape, style="filled", fillcolor=fillcolor)
    graph.add_node(attribute_node)
    graph.add_edge(pydot.Edge(entity_node, attribute_node, dir='none'))

# 保存图像
output_path = '/Users/firmamentwu/Downloads/旅游管理系统/ER-CHART/ER_diagram_high_quality_v2.png'
graph.write_png(output_path)

output_path
