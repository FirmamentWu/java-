import pydot
import os

# 定义表节点及其字段
tables = {
    "admins": [
        ("id", "int (PK)", "yellow"),
        ("username", "varchar(50)", "white"),
        ("pwd", "varchar(50)", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "difangmeishi": [
        ("id", "int (PK)", "yellow"),
        ("meishibianhao", "varchar(50)", "white"),
        ("mingcheng", "varchar(255)", "white"),
        ("fujinjingdian", "varchar(255)", "white"),
        ("fenlei", "int (FK)", "lightblue"),
        ("tupian", "text", "white"),
        ("jiage", "decimal(18,2)", "white"),
        ("meishijianjie", "text", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "diqu": [
        ("id", "int (PK)", "yellow"),
        ("diqumingcheng", "varchar(255)", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "jingdianxinxi": [
        ("id", "int (PK)", "yellow"),
        ("jingdianbianhao", "varchar(50)", "white"),
        ("jingdianmingcheng", "varchar(255)", "white"),
        ("suoshudiqu", "int (FK)", "lightblue"),
        ("tupian", "text", "white"),
        ("kaifangshijian", "varchar(255)", "white"),
        ("fujinmeishi", "text", "white"),
        ("dizhi", "varchar(255)", "white"),
        ("piaojia", "decimal(18,2)", "white"),
        ("liulanliang", "int", "white"),
        ("miaoshu", "longtext", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "liuyanban": [
        ("id", "int (PK)", "yellow"),
        ("xingming", "varchar(50)", "white"),
        ("lianxidianhua", "varchar(50)", "white"),
        ("liuyanneirong", "text", "white"),
        ("liuyanren", "varchar(50)", "white"),
        ("huifuneirong", "text", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "lunbotu": [
        ("id", "int (PK)", "yellow"),
        ("title", "varchar(50)", "white"),
        ("image", "varchar(255)", "white"),
        ("url", "varchar(255)", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "lvyouxianlu": [
        ("id", "int (PK)", "yellow"),
        ("xianlubianhao", "varchar(50)", "white"),
        ("xianlumingcheng", "varchar(255)", "white"),
        ("tupian", "text", "white"),
        ("chufadi", "varchar(255)", "white"),
        ("tujingdi", "varchar(255)", "white"),
        ("zhongdian", "varchar(255)", "white"),
        ("jiage", "decimal(18,2)", "white"),
        ("liulanliang", "int", "white"),
        ("xianlutese", "longtext", "white"),
        ("xianlujianjie", "longtext", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "meishifenlei": [
        ("id", "int (PK)", "yellow"),
        ("fenleimingcheng", "varchar(255)", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "shoucangjilu": [
        ("id", "int (PK)", "yellow"),
        ("username", "varchar(255)", "white"),
        ("xwid", "int (FK)", "lightblue"),
        ("biao", "varchar(255)", "white"),
        ("biaoti", "varchar(255)", "white"),
        ("url", "varchar(512)", "white"),
        ("ziduan", "varchar(255)", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "token": [
        ("token", "char(32) (PK)", "yellow"),
        ("session", "text", "white"),
        ("cx", "varchar(50)", "white"),
        ("login", "varchar(50)", "white"),
        ("username", "varchar(50)", "white"),
        ("valueid", "varchar(50)", "white"),
        ("token_time", "timestamp", "white"),
    ],
    "xinwenfenlei": [
        ("id", "int (PK)", "yellow"),
        ("fenleimingcheng", "varchar(50)", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "xinwenxinxi": [
        ("id", "int (PK)", "yellow"),
        ("biaoti", "varchar(255)", "white"),
        ("fenlei", "int (FK)", "lightblue"),
        ("tupian", "varchar(255)", "white"),
        ("tianjiaren", "varchar(50)", "white"),
        ("dianjilv", "int", "white"),
        ("neirong", "longtext", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "yonghu": [
        ("id", "int (PK)", "yellow"),
        ("yonghuming", "varchar(50)", "white"),
        ("mima", "varchar(50)", "white"),
        ("xingming", "varchar(50)", "white"),
        ("xingbie", "varchar(255)", "white"),
        ("shouji", "varchar(50)", "white"),
        ("youxiang", "varchar(50)", "white"),
        ("shenfenzheng", "varchar(50)", "white"),
        ("touxiang", "varchar(255)", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "youqinglianjie": [
        ("id", "int (PK)", "yellow"),
        ("wangzhanmingcheng", "varchar(50)", "white"),
        ("wangzhi", "varchar(50)", "white"),
        ("addtime", "timestamp", "white"),
    ],
    "yuding": [
        ("id", "int (PK)", "yellow"),
        ("lvyouxianluid", "int (FK)", "lightblue"),
        ("xianlubianhao", "varchar(50)", "white"),
        ("xianlumingcheng", "varchar(255)", "white"),
        ("chufadi", "varchar(255)", "white"),
        ("tujingdi", "varchar(255)", "white"),
        ("zhongdian", "varchar(255)", "white"),
        ("jiage", "decimal(18,2)", "white"),
        ("dingdanhao", "varchar(50)", "white"),
        ("yudingshijian", "varchar(25)", "white"),
        ("yudingrenxingming", "varchar(50)", "white"),
        ("lianxifangshi", "varchar(50)", "white"),
        ("zhuangtai", "varchar(50)", "white"),
        ("beizhu", "text", "white"),
        ("yudingren", "varchar(50)", "white"),
        ("addtime", "timestamp", "white"),
        ("iszf", "varchar(10)", "white"),
    ],
}

# 创建输出目录
output_dir = "/Users/firmamentwu/Downloads/旅游管理系统/ER-CHART"
os.makedirs(output_dir, exist_ok=True)

# 为每个表生成单独的ER图
for table, attrs in tables.items():
    graph = pydot.Dot(graph_type='graph', dpi=600)
    entity_node = pydot.Node(table, shape="rectangle", style="filled", fillcolor="lightgrey")
    graph.add_node(entity_node)
    for attr, attr_type, fillcolor in attrs:
        attribute_node = pydot.Node(f"{attr}: {attr_type}", shape="ellipse", style="filled", fillcolor=fillcolor)
        graph.add_node(attribute_node)
        graph.add_edge(pydot.Edge(entity_node, attribute_node, dir='none'))
    
    # 保存图像
    output_path = os.path.join(output_dir, f"{table}_ER_diagram.png")
    graph.write_png(output_path)

output_dir
