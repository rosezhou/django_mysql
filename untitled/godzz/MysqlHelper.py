import pymysql

class mysqlhelper:
    def __init__(self,host,user,password,database,port=3306,charset='utf8'):
        '''
        :param host:链接地址
        :param user: 用户名
        :param password: 密码
        :param database: 链接的数据库名
        :param port: 端口号
        :param charset: 字符集
        '''
        self.host = host
        self.uesr = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def connect(self):
        #获取链接对象和执行对象
