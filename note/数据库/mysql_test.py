# 1.导入包
import pymysql


def execute_crud_sql(sql, data):
    # 2.连接MySQL服务
    conne = pymysql.Connect(
        user="root",  # The first four arguments is based on DB-API 2.0 recommendation.
        password="wdc123826715",
        host="127.0.0.1",
        database="orders",
        port=3306,
        charset="utf8"
    )

    # 3.创建游标对象
    cur = conne.cursor()

    try:
        # 4.编写sql语句
        # 5.使用游标对象调用sql语句
        cur.execute(sql, data)

        # 6.提交操作(针对增删改)
        conne.commit()

    except Exception as e:
        print(e)
        conne.rollback()

    finally:
        # 7.关闭游标对象
        cur.close()
        # 8.关闭连接
        conne.close()


def show_orders():
    # 2.连接MySQL服务
    conne = pymysql.Connect(
        user="root",  # The first four arguments is based on DB-API 2.0 recommendation.
        password="wdc123826715",
        host="127.0.0.1",
        database="orders",
        port=3306,
        charset="utf8"
    )

    # 3.创建游标对象
    cur = conne.cursor()

    try:
        # 4.编写sql语句
        sql = "select * from orders;"

        # 5.使用游标对象调用sql语句
        cur.execute(sql)

        # 6.获取查询的结果
        result = cur.fetchall()
        data_list = []
        for row in result:
            data_list.append(
                {'id': row[0],
                 'count': row[1],
                 'price': str(row[2]),
                 'freight': str(row[3]),
                 'user': row[4],
                 'status': row[5],
                 'time': str(row[6]),
                 }
            )

        print("查询结果:")
        for row in data_list:
            print(row)

    except Exception as e:
        print(e)
        conne.rollback()

    finally:
        # 7.关闭游标对象
        cur.close()
        # 8.关闭连接
        conne.close()


def add_orders(data):
    sql = "insert into orders values(%s,%s,%s,%s,%s,%s,%s)"
    execute_crud_sql(sql, data)


def update_orders(data):
    sql = """
        update orders
        set count=%s,price=%s,freight=%s,user=%s,status=%s,time=%s
        where id=%s
        """
    data.append(data.pop(0))
    execute_crud_sql(sql, data)


def delete_orders(data):
    sql = "delete from orders where id = %s"
    execute_crud_sql(sql, data)


if __name__ == '__main__':
    data = [5, 5, 1000.00, 10.00, 'bang', '待收货', '2010-05-25']
    # update_orders(data)
    # delete_orders(10)
    show_orders()
