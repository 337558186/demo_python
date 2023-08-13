"""
mysql连接
"""
import pymysql

# 创建连接
mysql = pymysql.connect(
    host='localhost',  # 连接地址, 本地
    user='test',    # 用户
    password='123456',  # 数据库密码
    port=3306,   # 端口,默认为3306
    charset='utf8',  # 编码
    database='test'  # 选择数据库
)
# 创建游标对象
db = mysql.cursor()

# 增
sql = "insert into item (item) values (%s);"
# sql = 'delete from student where name="小明";'  # 删
# sql = 'update student set name="小芳",age=20,gender="男" where id=2;'  # 改
# sql = 'select * from userinfo'  # 查

try:
    # 新增数据-多条
    date = ("test1","test2","test3")
    db.executemany(sql,date)

    # 查询所有数据
    sql = 'select * from item'
    db.execute(sql)   # 数据数量
    result = db.fetchall()

    # 格式化数据  添加表头
    list_result = []  # 存储转换后数据
    for i in result:
        date_list = list(i)  # [1,"test3"]

        #  获取表详情，字段名，长度，属性等
        des = db.description  #(('id', 3, None, 11, 11, 0, False), ('item', 253, None, 255, 255, 0, True))

        # 从列表des取item[0]元素 放入一个新的列表
        table_head = [item[0] for item in des]  # ["id","item"]

        # 打包为元组的列表，zip[将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表]
        zipped = zip(table_head, date_list)  # [("id",1),("item","test3")]
        #  转换为字典
        dict_result = dict(zipped)

        list_result.append(dict_result)  # 将字典添加到list_result中

    print(list_result, end='\n')
    mysql.commit() # 表示将修改操作提交到数据库
    print('成功')

except Exception as e:
    print('操作失败',e)
    mysql.rollback() # 表示不成功则回滚数据

# 游标关闭
db.close()

# 关闭连接
mysql.close()

