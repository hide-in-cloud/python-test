import re
import time
from miniWeb服务器.application import urls
import pymysql


def route(path):
    def function_out(func):
        urls.route_dict[path] = func

        def function_in(*args, **kwargs):
            return func(*args, **kwargs)

        return function_in

    return function_out


@route("/index.py")
# 1. route("/index.py")    -------->function_out 引用
# 2. @function_out
# 3. index = function_out(index)
# 当调用index()时-------->function_in
def index():
    with open("/pythonHello/miniWeb服务器/templates/index.html", encoding="utf-8") as file:
        response_body = file.read()
        conn = pymysql.connect(host="localhost", user="root", password="wdc123826715", database="stock_db")
        cur = conn.cursor()
        cur.execute("select * from info")
        data_mysql = ""
        for line in cur.fetchall():
            stock = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="000007"></td>
            </tr>
            """ % line
            data_mysql += stock

        cur.close()
        conn.close()

        response_body = re.sub("{%content%}", data_mysql, response_body)
    return response_body


@route("/center.py")
def center():
    with open("/pythonHello/miniWeb服务器/templates/center.html", encoding="utf-8") as file:
        response_body = file.read()
        # -- 数据库查询
        conn = pymysql.connect(host="localhost", user="root", password="wdc123826715", database="stock_db")
        cur = conn.cursor()
        cur.execute(
            "select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info "
            "from info i inner join focus f on i.id = f.id")
        data_mysql = ""
        for line in cur.fetchall():
            stock = """
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td><a type="button class="btn btn-default btn-xs" href="/update/000007.html">
                            <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
                        <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="000007"></td>
                    </tr>
                    """ % line
            data_mysql += stock

        cur.close()
        conn.close()

        response_body = re.sub("{%content%}", data_mysql, response_body)
    return response_body


@route("/getTime.py")
def getTime():
    response_body = "This is time: %s." % time.ctime()
    return response_body
