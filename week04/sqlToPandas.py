'''
1. SELECT * FROM data;

2. SELECT * FROM data LIMIT 10;

3. SELECT id FROM data;  //id 是 data 表的特定一列

4. SELECT COUNT(id) FROM data;

5. SELECT * FROM data WHERE id<1000 AND age>30;

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

8. SELECT * FROM table1 UNION SELECT * FROM table2;

9. DELETE FROM table1 WHERE id=10;

10. ALTER TABLE table1 DROP COLUMN column_name;
'''
import numpy as np
import pandas as pd

group = ['x', 'y', 'z']
df = pd.DataFrame({
    "id": [i for i in range(100)],
    "group":[group[x] for x in np.random.randint(0,len(group),100)] ,
    "salary":np.random.randint(5,50,100),
    "age":np.random.randint(15,50,100)
})
# print(df)

# SELECT * FROM data;
df

# SELECT * FROM data LIMIT 10;
print(df.loc[0:9])

# SELECT id FROM data;  //id 是 data 表的特定一列
id = 10
print(df.loc[id])

# SELECT COUNT(id) FROM data;

