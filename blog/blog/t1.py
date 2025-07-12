import pymysql
pymysql.install_as_MySQLdb()  # 确保在Django初始化之前调用
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()
# 然后尝试导入MySQLdb和连接
try:
    import MySQLdb
    print("MySQLdb 导入成功！")
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]
        print(f"MySQL版本: {version}")
except Exception as e:
    print(f"导入MySQLdb失败: {e}")