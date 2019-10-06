import pandas as pd
import pymysql

sql = "SELECT * FROM test2"

eng = pymysql.connect("XDAirShare",
                      "root",
                      "time4@FUN",
                      "SuperstoreSampleDB",
                      charset = "utf8")

df = pd.read_sql(sql, eng)

print(df)

