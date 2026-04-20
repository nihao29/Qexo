# Qexo 配置文件 - 适用于 Cloudflare Pages
import os

# 基础配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = "yuhai3737"  # 随便改一串随机字符
DEBUG = False
ALLOWED_HOSTS = ['*']

# 允许访问的域名
DOMAINS = [
    "127.0.0.1",
    "localhost",
    # 这里改成你的 Qexo 域名，例如：qexo-xxx.pages.dev
    "qq.tcip.dpdns.org"
]

# 数据库（SQLite 免费无需配置）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 静态文件
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 语言时区
LANGUAGE_CODE = 'zh-hansns'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True
