"""
@File    :settings.py
@Editor  : 百年
@Date    :2025/9/18 13:26 
"""

TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'root',
                'password': 'HHCzio20',
                'database': 'fastapi',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                'echo': True

            }
        }
    },
    'apps': {
        'models': {
            'models': ['models','aerich.models'],
            'default_connection': 'default',
        }
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}
