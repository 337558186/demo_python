"""
@Time ： 2023/5/24 11:32
@Auth ： 植树的牧羊人
@desc : sqlite测试
"""
import sqlite3

class SQLITE():

   ## 打开数据库连接
   conn = sqlite3.connect('sqlite.db')
   print("Opened database successfully");


   @classmethod
   def create_table(cls):
      ## 清除已存在的表 - company
      # cls.conn.execute('''DROP TABLE company''');
      # cls.conn.commit()

      ## 创建一个表 - company
      cls.conn.execute('''CREATE TABLE company
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);''')
      print("Table created successfully");
      cls.conn.commit()

   @classmethod
   def add(cls):
      # 插入数据
      cls.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (1, 'Maxsu', 27, 'Haikou', 20000.00 )");
      # 插入多条数据
      sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
               VALUES (?, ?, ?, ?, ? )"  # 其中问号为占位符
      date = [(2, 'Allen', 26, 'Shenzhen', 35000.00), (3, 'Weiwang', 23, 'Guangzhou', 22000.00),
              (4, 'Marklee', 25, 'Beijing', 45000.00)]
      cls.conn.executemany(sql, date)

      cls.conn.commit()
      cls.conn.close()
      print("Records Insert successfully");
      print('--------------------------- start fetch data from company --------------------------');


   @classmethod
   def select(cls):

      cursor = cls.conn.execute("SELECT id, name, address, salary  from COMPANY")
      for row in cursor:
         print ("ID = ", row[0])
         print ("NAME = ", row[1])
         print ("ADDRESS = ", row[2])
         print ("SALARY = ", row[3], "\n")

      print ("Select Operation done successfully.");

   @classmethod
   def select_by_id(cls):

      sql = "SELECT * FROM userinfo WHERE id = ?"
      # 加逗号  表示一个元组
      data_tuple = (1,)
      cls.conn.execute(sql,data_tuple)
      result = db.fetchmany(1)  # 一次查找1条

      #  获取表头,格式化数据为字典
      list_result = []
      for i in result:
         date_list = list(i)
         des = db.description  # 获取表详情，字段名，长度，属性等
         table_head = [item[0] for item in des]  # 获取表头
         dict_result = dict(zip(table_head, date_list))  # 打包为元组的列表 再转换为字典
         list_result.append(dict_result)  # 将字典添加到list_result中

      return list_result



if __name__ == '__main__':

   SQLITE.select()







