import pydot
from IPython.display import Image

# 创建一个新的有向图
graph = pydot.Dot(graph_type='digraph', rankdir='LR')

# 定义表的节点
table_node = pydot.Node("jingdianxinxi", shape="record", 
                        label="{ jingdianxinxi | { id: int (PK) | jingdianbianhao: varchar(50) | jingdianmingcheng: varchar(255) | suoshudiqu: int (FK) | tupian: text | kaifangshijian: varchar(255) | fujinmeishi: text | dizhi: varchar(255) | piaojia: decimal(18, 2) | liulanliang: int | miaoshu: longtext | addtime: timestamp } }")
graph.add_node(table_node)

# 创建并显示图像
graph.write_png('/Users/firmamentwu/Downloads/旅游管理系统/ER-CHART/ER_diagram.png')
Image(filename='/Users/firmamentwu/Downloads/旅游管理系统/ER-CHART/ER_diagram.png')
