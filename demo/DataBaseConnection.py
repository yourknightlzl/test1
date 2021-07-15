# 数据库连接
import pymysql  # 导入mysql数据库

# 连接数据库
conn = pymysql.connect(
    host='193.112.240.108',
    port=4000,
    user='root',
    password='Getmind1107',
    database='test_dnet_biz',
    charset='utf8'
)

# 定义一个光标
cursor = None


# 查询订单号  5bce80ae11b9ae5b6257d9ca（好快收) ，5bc18e47dc5c6a48a7743612（fss222),5bc18e47dc5c6a48a7743621(fdss)
def selectOrder():
    # SQL语句
    sql = "SELECT okey 订单号,otime11,umname FROM omr_odr_order WHERE uacc = '5bc18e47dc5c6a48a7743612' " \
          "ORDER BY otime11 desc LIMIT 0,1"

    cursor = returnCursor(sql)
    # 获取查询结果
    ret1 = cursor.fetchone()
    closeConnection(cursor)
    return ret1


# 查询最新的打印编码code
# orderType 判断是否为一单多机
def printCode(orderType):
    # SQL语句 获取最新添加的code码
    sql = ''
    cursor = ''
    ret2 = ''
    if orderType == "一键回收":
        sql = "SELECT code  FROM prd_code order by atime desc LIMIT 0,2"
        cursor = returnCursor(sql)
        ret2 = cursor.fetchall()
    else:
        sql = "SELECT code  FROM prd_code order by atime desc LIMIT 0,1"
        cursor = returnCursor(sql)
        ret2 = cursor.fetchone()
    closeConnection(cursor)
    return ret2

# 根据库存编码搜索对应的机型
def selectModel(code):
    # SQL语句  根据库存编码获取机型
    sql = "SELECT pname FROM prd_product WHERE bcode = '"+code+"'"
    cursor = returnCursor(sql)
    # 获取查询结果
    ret3 = cursor.fetchone()
    # 关闭连接
    closeConnection(cursor)
    return ret3

# 获取一个游标
def returnCursor(sql):
    # 获取一个光标，返回字典数据类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        # 拼接并执行SQL语句
        cursor.execute(sql)
    except:
        # 如果mysql连接超时就重新连接
        conn.ping()
        # 拼接并执行SQL语句
        cursor.execute(sql)
    return cursor


# 关闭连接方法
def closeConnection(cursor):
    # 关闭连接
    cursor.close()
    conn.close()

if __name__ == "__main__":
    orderType = '一键回收'
    codes = printCode(orderType)
    for i in codes:
        print(i['code'])