"""
@File    :config.py
@Editor  : 百年
@Date    :2025/11/26 8:37 
"""
import os
class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # 读取.env文件中的配置
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 2. 禁用追踪修改（强烈建议关闭，节省性能）
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 3. 是否打印 SQL 语句（开发时有用）
    SQLALCHEMY_ECHO = True  # 开发时打开，生产关闭

    # 4. 连接池大小（默认 10）
    SQLALCHEMY_POOL_SIZE = 30

    # 5. 连接池超时时间（秒）
    SQLALCHEMY_POOL_TIMEOUT = 30

    # 6. 连接空闲多久后自动断开（秒）
    SQLALCHEMY_POOL_RECYCLE = 1800  # 30分钟

    # 7. 启用连接池预检（防止 MySQL 8小时断开）
    SQLALCHEMY_POOL_PRE_PING = True  # 推荐开启
    #
    # # 8. 是否自动提交事务（一般不开启，手动控制更好）
    # # SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # 已废弃，不推荐使用
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:HHCzio20@127.0.0.1:3306/api2'
    #
    # # 9.设置session需要的SECRET_KEY
    SECRET_KEY = ';ouahsef;euahiuhiluh'
    #部署
    # 10.配置项目路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # important:得到当前文件的文件夹
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATES_DIR = os.path.join(STATIC_DIR, 'templates')
    # 头像上传目录
    UPLOAD_ICON_FOLDER = os.path.join(STATIC_DIR, 'upload\icon')
    # 相册上传目录
    # UPLOAD_PHOTO_FOLDER = os.path.join(STATIC_DIR, 'upload\icon')



# 配置开发配置
class devConfig(Config):
    DEBUG = True
    ENV = 'development'


# 配置生产配置
class prodConfig(Config):
    DEBUG = False
    ENV = 'production'


# 映射字典
configdict = {
    'development': devConfig,
    'production': prodConfig,
    'default': devConfig
}