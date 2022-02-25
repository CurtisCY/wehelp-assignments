# Learn the SQL Connection Pool

## Follow the step below to create SQL connection pool:  
https://dev.mysql.com/doc/connector-python/en/connector-python-connection-pooling.html

## The benefit of using SQL connection pool instead of creating connection directly to the SQL database:
1. Connection Pool can help you keep/maintain the connection (open/close) between your application and the database
2. Connection Pool can setup maximum connection number which avoid your application exceed the allowed connection number of the database
3. Connection Pool can check the availabily of the connection to the database and recover once the connection break.

### Import mysql.connector.pooling
```mysql
import mysql.connector.pooling
```

### Configure Database and create connection pool - cnxpool 

```mysql
cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "sqlCnxPool",
                                                      pool_size = 10,
                                                      **dbconfig)

cnx1 = cnxpool.get_connection()
mycursor = cnx1.cursor()
mycursor1 = cnx1.cursor()
mycursor2 = cnx1.cursor()
mycursor3 = cnx1.cursor()                                             
```


### Establish a connection to connection pool and call cursor() function
```mysql
cnx1 = cnxpool.get_connection()
mycursor = cnx1.cursor()
```
