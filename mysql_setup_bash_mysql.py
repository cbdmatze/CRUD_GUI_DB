'''

AirvonMatthias:CRUD_GUI_DB martinawill$ brew services start mysql
==> Tapping homebrew/services
Cloning into '/opt/homebrew/Library/Taps/homebrew/homebrew-services'...
remote: Enumerating objects: 3902, done.
remote: Counting objects: 100% (495/495), done.
remote: Compressing objects: 100% (163/163), done.
remote: Total 3902 (delta 401), reused 333 (delta 332), pack-reused 3407 (from 2)
Receiving objects: 100% (3902/3902), 1.16 MiB | 7.09 MiB/s, done.
Resolving deltas: 100% (1891/1891), done.
Tapped 2 commands (53 files, 1.4MB).
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)
AirvonMatthias:CRUD_GUI_DB martinawill$ CREATE DATABASE moviewebapp
bash: CREATE: command not found
AirvonMatthias:CRUD_GUI_DB martinawill$ mysql_secure_installation

Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 2
Please set the password for root here.

New password: 

Re-enter new password: 

Estimated strength of the password: 100 
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : n

 ... skipping.
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.

Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
Success.

All done! 
AirvonMatthias:CRUD_GUI_DB martinawill$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 9.1.0 Homebrew

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE moviewebapp;
Query OK, 1 row affected (0.10 sec)

mysql> SHOW DATABASE;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'DATABASE' at line 1
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| moviewebapp        |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.04 sec)

mysql> USE moviewebapp
Database changed
mysql> CREATE TABLE movies (
    -> 
Display all 764 possibilities? (y or n) 
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(100) NOT NULL,
    -> director VARCHAR(100) NOT NULL,
    -> year INT NOT NULL,
    -> rating DECIMAL(3,1) NOT NULL
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> SHOW TABLES
    -> DESCRIBE moviewebapp
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'DESCRIBE moviewebapp' at line 2
mysql> SHOW TABLES;
+-----------------------+
| Tables_in_moviewebapp |
+-----------------------+
| movies                |
+-----------------------+
1 row in set (0.00 sec)

mysql> DESCRIBE movies;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| name     | varchar(100) | NO   |     | NULL    |                |
| director | varchar(100) | NO   |     | NULL    |                |
| year     | int          | NO   |     | NULL    |                |
| rating   | decimal(3,1) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0.01 sec)

mysql> CREATE TABLE users (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(100) NOT NULL
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> SHOW TABLES;
+-----------------------+
| Tables_in_moviewebapp |
+-----------------------+
| movies                |
| users                 |
+-----------------------+
2 rows in set (0.00 sec)

mysql> DESCRIBE users;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(100) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> 

'''

'''
# UPDATE DATA 

UPDATE users
SET id = (new_value), name = (new_value)
WHERE id = (original_value);





'''