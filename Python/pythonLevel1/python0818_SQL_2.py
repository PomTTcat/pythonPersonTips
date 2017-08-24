# -*- coding: utf-8 -*-

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
               '00', 'Jeff', 26, 'Beijing'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '01', 'JeffGods', 26, 'Beijing'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '02', 'Jack', 32, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '03', 'JackMan', 22, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '04', 'Tom', 26, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '05', 'JeffIn', 26, 'Beijing'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '06', 'Jack', 32, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '07', 'JackMan', 22, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '08', 'Tom', 26, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '09', 'JeffOn', 26, 'Beijing'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '10', 'Jack', 32, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '11', 'JackMan', 22, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '12', 'Tom', 26, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '13', 'JeffOFF', 26, 'Beijing'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '14', 'Jack', 32, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '15', 'JackMan', 22, 'Shanghai'])
cursor.execute('insert into table0818 (id, name, age, city) values (%s, %s, %s, %s)', [
               '16', 'Tom', 26, 'TaiZhou'])

cursor.execute('select * from table0818')
print cursor.fetchall()

print '--------LIMIT---------'  # 要返回的记录的数目
cursor.execute('SELECT * FROM table0818 LIMIT 5')
print cursor.fetchall()

print '--------LIKE---------'  # 返回 city 末尾是g
print '--------SQL 通配符---------'
cursor.execute('SELECT * FROM table0818 WHERE City LIKE %s', ('%g',))
print cursor.fetchall()

# 中间有 Zh 的值
cursor.execute('SELECT * FROM table0818 WHERE City LIKE %s', ('%Zh%',))
print cursor.fetchall()

# 不带 ei
cursor.execute(
    'SELECT * FROM table0818 WHERE City Not LIKE %s and City Not LIKE %s', ('%ei%', '%hang%'))
print cursor.fetchall()

# %	替代一个或多个字符
# _	仅替代一个字符
# [charlist]	字符列中的任何单一字符					#[ALN]% 以A,L,N开头的都行。
# [^charlist]或者[!charlist]不在字符列中的任何单一字符	#[!ALN]% 不以A,L,N开头的都行。

print '--------IN 操作符---------'  # IN 操作符允许我们在 WHERE 子句中规定多个值


def getName(x):
    cursor.execute('SELECT * FROM table0818 WHERE name = %s', (x,))
    print cursor.fetchall()

getName('Jeff')

ssss = ('SELECT * FROM table0818 WHERE name = %s', ('Jeff',))
# cursor.execute('SELECT * FROM table0818 WHERE name = %s', ('Jeff',))
cursor.execute(*ssss)
print cursor.fetchall()

cursor.execute('SELECT * FROM table0818 WHERE name in (%s,%s)',
               ('Jeff', 'JeffGods'))
print cursor.fetchall()

print '--------BETWEEN---------'
# cursor.execute('SELECT * from table0818 where name between %s and %s',
# ('Jeff','Jack')) # not work here
cursor.execute('SELECT * from table0818 where id between %s and %s', (1, 5))
# cursor.execute('SELECT * from table0818 where id not between %s and %s',
# (1,5)) # 显示范围之外的人
print cursor.fetchall()

print '--------Alias---------'

# 表的 SQL Alias 语法 .别名使查询程序更易阅读和书写。
cursor.execute('SELECT tp.name,tp.age FROM table0818 AS tp')
print cursor.fetchall()

print '---------------------'
cursor.execute('SELECT name AS FamilyName FROM table0818')
print cursor.fetchall()

print '--------JOIN---------'  # 不要用，尽量查两次
cursor.execute('DROP TABLE tableJoin')
cursor.execute(
    'create table tableJoin (id_o varchar(20) primary key, OrderNo int,id int)')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into tableJoin (id_o, OrderNo, id) values (%s, %s, %s)', [
               '1', '1234', 03])
cursor.execute('insert into tableJoin (id_o, OrderNo, id) values (%s, %s, %s)', [
               '2', '1235', 01])
cursor.execute('insert into tableJoin (id_o, OrderNo, id) values (%s, %s, %s)', [
               '3', '1236', 03])

cursor.execute(
    'SELECT table0818.id, table0818.name, tableJoin.OrderNo '
    'FROM table0818, tableJoin '
    'WHERE table0818.id = tableJoin.id')
print cursor.fetchall()

print '--------INNER JOIN---------'
cursor.execute(
    'SELECT table0818.id, table0818.name, tableJoin.OrderNo '
    'FROM table0818 '
    'INNER JOIN tableJoin '
    'ON table0818.id = tableJoin.id '
    'ORDER BY table0818.id')
print cursor.fetchall()

# 从左表 (table_name1) 那里返回所有的行，即使在右表 (table_name2) 中没有匹配的行。
print '--------LEFT JOIN---------'
cursor.execute(
    'SELECT table0818.id, table0818.name, tableJoin.OrderNo '
    'FROM table0818 '
    'LEFT JOIN tableJoin '
    'ON table0818.id = tableJoin.id '
    'ORDER BY table0818.id')
print cursor.fetchall()
# 第一个表的id 没有在第二个表中出现，第一表也打印出来。

print '--------RIGHT JOIN---------'  # 和left join类似。
cursor.execute(
    'SELECT table0818.id, table0818.name, tableJoin.OrderNo '
    'FROM table0818 '
    'RIGHT JOIN tableJoin '
    'ON table0818.id = tableJoin.id '
    'ORDER BY table0818.id')
print cursor.fetchall()
# 第一个表的id 没有在第二个表中出现，第一表也打印出来。

print '--------FULL JOIN---------'  # 只要其中某个表存在匹配，FULL JOIN 关键字就会返回行。

print '--------UNION---------'  # UNION 操作符用于合并两个或多个 SELECT 语句的结果集。
# 必须拥有相同数量的列
# 拥有相似的数据类型

print '--------SELECT INTO---------'
''' 制作备份复件
SELECT *
INTO Persons_backup
FROM Persons

# IN 子句可用于向另一个数据库中拷贝表 把Persons 拷贝到 Backup.mdb 中的 Persons中。
SELECT *
INTO Persons IN 'Backup.mdb'
FROM Persons

# 如果我们希望拷贝某些域，可以在 SELECT 语句后列出这些域：
SELECT LastName,FirstName
INTO Persons_backup
FROM Persons

# "Persons" 表中提取居住在 "Beijing" 的人的信息，创建了一个带有两个列的名为 "Persons_backup" 的表
SELECT LastName,Firstname
INTO Persons_backup
FROM Persons
WHERE City='Beijing'

'''


print '--------SQL CREATE DATABASE 语句---------'
# CREATE DATABASE my_db

print '--------SQL CREATE TABLE 语句---------'

print '--------SQL VIEW---------'

# SQL 撤销视图
cursor.execute('DROP VIEW testView')
cursor.execute(
    'CREATE VIEW testView AS '
    'SELECT id,name '
    'FROM table0818 '
    'Where city = %s', ('Shanghai',))
print cursor.execute('SELECT * FROM testView')
print cursor.fetchall

# cursor.execute('select * from table0818')
# print cursor.fetchall()

print '--------更新 VIEW---------'


'''
SQL CREATE OR REPLACE VIEW Syntax
CREATE OR REPLACE VIEW view_name AS
SELECT column_name(s)
FROM table_name
WHERE condition

希望向 "Current Product List" 视图添加 "Category" 列
CREATE VIEW [Current Product List] AS
SELECT ProductID,ProductName,Category
FROM Products
WHERE Discontinued=No

'''

# cursor.close()
# conn.close()
