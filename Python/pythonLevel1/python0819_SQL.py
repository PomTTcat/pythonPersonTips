# -*- coding: utf-8 -*-

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(
    user='root', password='newpass', database='test', use_unicode=True)
cursor = conn.cursor()


# 先删除表，再创建user表:
# cursor.execute('DROP TABLE Orders')
cursor.execute('DROP TABLE if exists Orders')
cursor.execute(
    'create table Orders '
    '(id int NOT NULL AUTO_INCREMENT, '
    'name varchar(20), '
    'age int, '
    'city varchar(30), '
    'salary int, '
    'percent decimal, '
    'PRIMARY KEY (id)'
    ')')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into Orders (name, age, city, salary,percent) values (%s, %s, %s, %s, %s)', [
               'Jeff', 26, 'Beijing', 15000, 1002.23])
cursor.execute('insert into Orders (name, age, city, salary) values (%s, %s, %s, %s)', [
               'Jeffery', 27, 'Beijing', 20000])
cursor.execute('insert into Orders (name, age, city, salary) values (%s, %s, %s, %s)', [
               'JackMan', 28, 'Beijing', 25000])
cursor.execute('insert into Orders (name, age, city, salary) values (%s, %s, %s, %s)', [
               'Jack', 28, 'Beijing', 30000])
cursor.execute('insert into Orders (name, age, city, salary) values (%s, %s, %s, %s)', [
               'Jack', 28, 'Guangdong', 27000])

print '--------AVG()---------'
cursor.execute('SELECT AVG(salary) FROM Orders')
print cursor.fetchall()

cursor.execute('SELECT name FROM Orders '
               'WHERE salary>(SELECT AVG(salary) FROM Orders)')
print cursor.fetchall()

print '--------COUNT()---------'  # 叫jack的有几个。
cursor.execute('SELECT COUNT(name) AS CustomerNilsen FROM Orders '
               'WHERE name=%s', ('jack',))
print cursor.column_names
print cursor.fetchall()
print dir(cursor)

print '--------FIRST()---------'  # mysql没有first()这个函数。
cursor.execute('SELECT name FROM Orders '
               'where id = 1')
print cursor.fetchall()


print '--------last()---------'  # mysql没有last()这个函数。
cursor.execute('SELECT name FROM Orders '
               'order by %s Desc ', ('id',))
print cursor.fetchall()


cursor.execute('SELECT name FROM Orders '
               'where %s = (select max(%s)) limit 1', ('id', 'id'))
print cursor.fetchall()

print '--------MAX()---------'
cursor.execute('SELECT MAX(salary) AS LargestOrderPrice FROM Orders')
print cursor.fetchall()

print '--------MIN()---------'
cursor.execute('SELECT MIN(salary) AS LargestOrderPrice FROM Orders')
print cursor.fetchall()

print '--------SUM()---------'
cursor.execute('SELECT SUM(salary) AS LargestOrderPrice FROM Orders')
print cursor.fetchall()

print '--------GROUP BY()---------'
cursor.execute('SELECT name,SUM(salary) FROM Orders')
print cursor.fetchall()

# 可以看出必须用 GROUP BY name
cursor.execute('SELECT name,SUM(salary) FROM Orders '
               'GROUP BY name')
print cursor.fetchall()

print '--------HAVING()---------' # 总消费低于20000的。
# 在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与合计函数一起使用。
cursor.execute('SELECT name,SUM(salary) FROM Orders '
               'GROUP BY name '
               'HAVING SUM(salary)<20000')
print cursor.fetchall()


print '--------UCASE()---------' # 字母变成大写的
cursor.execute('SELECT UCASE(name),salary FROM Orders')
print cursor.fetchall()

print '--------LCASE()---------' # 字母变成小写的

print '--------MID()---------'	# 切割字符串而已
cursor.execute('SELECT MID(City,1,3) as SmallCity FROM Orders')
print cursor.fetchall()

print '--------LEN()---------'	
cursor.execute('SELECT  CHAR_LENGTH(City) FROM Orders')
print cursor.fetchall()

print '--------FORMAT()---------' # 去掉百分号的值	
cursor.execute('SELECT  FORMAT(percent,0) FROM Orders')
print cursor.fetchall()

print '--------Now()---------'	
cursor.execute('SELECT name, salary, Now() as PerDate FROM Orders')
print cursor.fetchall()


print '--------Now() + FORMAT()---------' # 去掉百分号的值	
cursor.execute('SELECT name, salary, FORMAT(Now(),%s) as PerDate '
	'FROM Orders',('YYYY-MM-DD',))
print cursor.fetchall()


# 关闭Cursor和Connection:
cursor.close()
conn.close()
# 什么情况下需要用%s？
'''
创建一行数据时：value
条件。比如order，where

'''
