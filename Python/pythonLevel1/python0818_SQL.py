# -*- coding: utf-8 -*-

import sys
print sys.path

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(
    user='root', password='newpass', database='test', use_unicode=True)
cursor = conn.cursor()


# 先删除表，再创建user表:
cursor.execute('DROP TABLE table0818')
cursor.execute(
    'create table table0818 (id varchar(20) primary key, name varchar(20),age int,city varchar(30))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '1', 'Jeff', 26, 'Beijing'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '2', 'Jack', 32, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '3', 'JackMan', 22, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '4', 'Tom', 26, 'Shanghai'])

print cursor.rowcount

# 提交事务:
# conn.commit()
# cursor.close()


# 运行查询:select
cursor = conn.cursor()
cursor.execute('select * from table0818')
print cursor.fetchall()

cursor.execute('select * from table0818 where id = %s', ('1',))
print cursor.fetchall()

cursor.execute('select id,name from table0818 where id = %s', ('1',))
print cursor.fetchall()

# DISTINCT 关键词		列出不同（distinct）的值
cursor.execute('SELECT DISTINCT city FROM table0818')
print cursor.fetchall()

# WHERE 子句. 数字加不加双引号都可以，字符串必须加
# 大部分数据库系统也接受双引号!!!!!
cursor.execute('SELECT * FROM table0818 WHERE City = %s', ('Shanghai',))
print cursor.fetchall()

cursor.execute('SELECT * FROM table0818 WHERE age = %s', (26,))
print cursor.fetchall()

print '--------between---------'
cursor.execute('SELECT * FROM table0818 WHERE age between %s and %s', (25, 50))
print cursor.fetchall()

print '--------AND 和 OR 运算符---------'
cursor.execute(
    'SELECT * FROM table0818 WHERE age = %s and city = %s', (26, 'Beijing'))
print cursor.fetchall()

# OR 差不多。

print '--------SQL ORDER BY-----依据名字字母排序----'
cursor.execute('SELECT name, city FROM table0818 ORDER BY name')
# cursor.execute('SELECT name, city FROM table0818 ORDER BY name desc') #
# + desc 逆序

# 以逆字母顺序显示公司名称，并以数字顺序显示顺序号：
# SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC,
# OrderNumber ASC
print cursor.fetchall()


print '--------before UPDATE---------'
cursor.execute('select * from table0818')
print cursor.fetchall()

print '--------UPDATE 语句---------------------------'
cursor.execute('UPDATE table0818 SET city = %s WHERE id = %s',
               ('Gods', 1))
# print cursor.fetchall()	# No result set to fetch from.

print '--------after UPDATE---------------------------'
cursor.execute('select * from table0818')
print cursor.fetchall()

print '--------delete---------'
cursor.execute('DELETE FROM table0818 WHERE name = %s', ('JackMan',))
# print cursor.fetchall() # No result set to fetch from.

print '--------after delete---------------------------'
cursor.execute('select * from table0818')
print cursor.fetchall()

# 不删除表的情况下删除所有的行。这意味着表的结构、属性和索引都是完整的：
cursor.execute('DELETE FROM table0818')
cursor.execute('select * from table0818')
print cursor.fetchall()

# 关闭Cursor和Connection:
cursor.close()
conn.close()
