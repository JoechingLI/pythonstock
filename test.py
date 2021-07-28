
from datetime import datetime, timedelta, time  # 时间处理函数
import pymysql  # mysql操作库
import pandas as pd
import numpy as np
import tushare as ts

#
# # 生产环境mysql配置
# mysqlSetting_server = {
#     'host': "IP",
#     'port': 3306,
#     'user': "root",
#     'passwd': "********",
#     'db': "Finance",
#     'charset': 'utf8'
# }
# 本地
mysqlSetting_local = {
    'host': "localhost",
    'port': 3306,
    'user': "root",
    'passwd': "123456",
    'db': "stock_db",
    'charset': 'utf8'
}


# 执行sql语句
def exeSql(mysqlSetting, sql):
    # 打开数据库连接
    db = pymysql.connect(host=mysqlSetting['host'], port=mysqlSetting['port'], user=mysqlSetting['user'], \
                         passwd=mysqlSetting['passwd'], db=mysqlSetting['db'], charset=mysqlSetting['charset'])
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor.execute(sql)
    ret = cursor.fetchall()
    db.commit()

    # 关闭数据库连接
    db.close()
    return ret


# DataFrame对象落地数据库
def df2sql(mysqlSetting, df, tableName):
    # 打开数据库连接
    db = pymysql.connect(host=mysqlSetting['host'], port=mysqlSetting['port'], user=mysqlSetting['user'], \
                         passwd=mysqlSetting['passwd'], db=mysqlSetting['db'], charset=mysqlSetting['charset'])

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 添加操作的sql语句
    sqlInsert = "REPLACE INTO " + tableName + " ("
    for _, column in enumerate(df.columns):
        if _ < len(df.columns) - 1:
            sqlInsert = sqlInsert + column + ','
        else:
            sqlInsert = sqlInsert + column + ') VALUES '
    for index, row in df.iterrows():
        sqlInsertNew = sqlInsert + '('
        for i, column in enumerate(df.columns):
            if i < len(df.columns) - 1:
                if pd.isnull(row[column]) or row[column] == 0:
                    sqlInsertNew = sqlInsertNew + 'NULL' + ','
                else:
                    sqlInsertNew = sqlInsertNew + '\'' + str(row[column]).replace('\'', '') + '\'' + ','
                    # sqlInsertNew=sqlInsertNew+'\''+str(row[column])+'\''+','
            else:
                if pd.isnull(row[column]) or row[column] == 0:
                    sqlInsertNew = sqlInsertNew + 'NULL'
                else:
                    sqlInsertNew = sqlInsertNew + '\'' + str(row[column]).replace('\'', '') + '\''
                    # sqlInsertNew=sqlInsertNew+'\''+str(row[column])+'\''
        sqlInsertNew = sqlInsertNew + ');'
        print(sqlInsertNew)
        cursor.execute(sqlInsertNew)
    db.commit()

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    ts.set_token('797d4544a4a2afa27145a385b7e48a3e1b49d92b800460ca4220e402')
    pro = ts.pro_api()
    data = pro.query('stock_company', exchange='SZSE', list_status='L',
                     fields='ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope')  # 修改exchange可以获取上交所的股票
    df2sql(mysqlSetting_local, data, "companyInfoTable")
