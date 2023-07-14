user_permission = 9  # 1001
"""二进制表示"""
# 判断对应权限 : 用户因子 & 权限因子 != 0
DEL_PERMISSION = 8  # 1000
READ_PERMISSION = 4  # 0100
WRITE_PERMISSION = 2  # 0010
EXE_PERMISSION = 1  # 0001


def check_permission(x, y):
    # print("最外层")

    def handle_action(func):
        # print("第二层")

        def do_action(*args, **kwargs):
            # print("最内层")
            if x & y != 0:
                func(*args, **kwargs)
            else:
                print("对不起，您没有相应的权限")

        return do_action

    return handle_action


@check_permission(user_permission, READ_PERMISSION)
def read():
    print("正在读文件")


@check_permission(user_permission, WRITE_PERMISSION)
def write():
    print("正在写文件")


@check_permission(user_permission, EXE_PERMISSION)
def execute():
    print("正在执行文件")


@check_permission(user_permission, DEL_PERMISSION)
def delete():
    print("正在删除文件")


read()
write()
execute()
delete()
