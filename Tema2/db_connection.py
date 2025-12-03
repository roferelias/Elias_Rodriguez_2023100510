import pymysql
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',
        port=3308,
        user='root',
        password='admin123',
        database='ganado',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
