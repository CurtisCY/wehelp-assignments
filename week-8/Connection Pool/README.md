# Learn the SQL Connection Pool
Cancel changes
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
dbconfig = {
  "host": "localhost",
  "user": os.getenv('SQLUSER'), #Read username/password from environment variable
  "password": os.getenv('SQLPASSWORD'),
  "database": "week6"
}

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "sqlCnxPool",
                                                      pool_size = 10,
                                                      **dbconfig)

cnx1 = cnxpool.get_connection()
cnx2 = cnxpool.get_connection()
cnx3 = cnxpool.get_connection()
cnx4 = cnxpool.get_connection()
                                           
```


### Establish a connection to connection pool and call cursor() function
```mysql
mycursor = cnx1.cursor()
# mycursor.execute(f"SELECT name, username, password FROM member WHERE username='{usernameInput}' AND password='{passwordInput}'")
mycursor.execute("SELECT name, username, password FROM member WHERE username=%s AND password=%s",(usernameInput,passwordInput,))
myresult = mycursor.fetchall()
```
