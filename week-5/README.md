
**3-1 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料**

~~~mysql
INSERT INTO member
(name, username, password, time)
VALUES
("Curtis", "test", "test", NOW());
~~~
![image](https://user-images.githubusercontent.com/63384830/151683920-407bbfa6-e4ef-43de-978d-14e232ea5e5c.png)

**3-2 使用 SELECT 指令取得所有在 member 資料表中的會員資料**

~~~mysql
SELECT * FROM member
~~~
![image](https://user-images.githubusercontent.com/63384830/151683947-9f399b73-9d4e-4a55-b1d9-ccfadfb0317c.png)

**3-3 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序**

~~~mysql
SELECT * FROM member ORDER BY time DESC;
~~~
![image](https://user-images.githubusercontent.com/63384830/151683968-40995279-238f-4a36-b3b7-17b2cc4075f2.png)

**3-4 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )**

~~~mysql
SELECT * FROM member WHERE id BETWEEN 2 AND 4 ORDER BY time DESC;
~~~
![image](https://user-images.githubusercontent.com/63384830/151683984-266a4b5b-2ea4-4283-9800-101b8b8f4903.png)

**3-5 使用 SELECT 指令取得欄位 username 是 test 的會員資料**

~~~mysql
SELECT * FROM member WHERE username='test';
~~~
![image](https://user-images.githubusercontent.com/63384830/151684001-7aea0774-83f5-40c3-8292-2c320d0b1880.png)

**3-6 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料**

~~~mysql
SELECT * FROM member WHERE username='test' AND password='test';
~~~
![image](https://user-images.githubusercontent.com/63384830/151684007-a7fb9052-744f-4b85-986d-01476e02f111.png)

**3-7 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2**

~~~mysql
UPDATE member SET name='test2' WHERE username='test'
~~~
![image](https://user-images.githubusercontent.com/63384830/151684024-3fed8909-d51f-46d0-abeb-fac99cadcf2f.png)

**4-1 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 ) **

~~~mysql
SELECT COUNT(*) AS 總會員數 FROM member;
~~~
![image](https://user-images.githubusercontent.com/63384830/151684362-a429c745-6364-4a86-af82-17e3a375105e.png)

**4-2 取得 member 資料表中，所有會員 follower_count 欄位的總和 **

~~~mysql
SELECT SUM(follower_count) AS 追蹤者數量總和 FROM member;
~~~
![image](https://user-images.githubusercontent.com/63384830/151684380-47b2a473-20cd-469f-b2ea-41517f778ed0.png)

**4-3 取得 member 資料表中，所有會員 follower_count 欄位的平均數 **

~~~mysql
SELECT AVG(follower_count) AS 會員追蹤者數量平均值 FROM member;
~~~
![image](https://user-images.githubusercontent.com/63384830/151684426-4f4e12ea-8e8d-4a1d-89b2-915b0fab3557.png)

