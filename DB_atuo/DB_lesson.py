import pymysql
class DB_utils():
    def __init__(self):
        self.host="192.168.1.30"
        self.user="juan"
        self.password="123456"
        self.database="dcs"
        self.port=3306
    def get_connect(self):
        db=pymysql.Connect(host=self.host,user=self.user,password=self.password,port=self.port,database=self.database)
        return db
    def select_sql(self,sql):
        db1=self.get_connect()
        a = db1.cursor()
        a.execute(sql)
        all=a.fetchall()
        print(all)
    def insert_sql(self,sql):
        db1 = self.get_connect()
        a = db1.cursor()
        a.execute("select * from mytest;")
        all_1 = a.fetchall()
        print(all_1)
        a.execute(sql)
        a.execute("select * from mytest;")
        all_2=a.fetchall()
        print(all_2)
    def del_sql(self,sql):
        db1 = self.get_connect()
        a = db1.cursor()     #建立游标对象
        a.execute("select * from mytest;")  #操作sql语句，获取sql语句返回的值，装在a身上
        all_1 = a.fetchall()                #通过a.fetchall,获取a身上全部的信息，并赋值给all
        print(all_1)                        #输出all，也可以不赋值给all，直接输出：a.fetchall
        a.execute(sql)
        a.execute("select * from mytest;")
        all_2 = a.fetchall()
        print(all_2)



m=DB_utils()
# m.select_sql("select * from mytest;")
# m.insert_sql("insert into mytest values(5,'小吴',27);")
m.del_sql("delete from mytest where id=2")

