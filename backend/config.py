import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    MODEL_API_URL = os.getenv('MODEL_API_URL', 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions')
    DASHSCOPE_API_KEY = os.getenv('DASHSCOPE_API_KEY', 'sk-tmp')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:your_password@localhost/software_db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    PERMISSION_CODE = os.getenv('PERMISSION_CODE', 'your_permission_code')
    AMAP_API_KEY = os.getenv('AMAP_API_KEY', 'your_amap_api_key')
    AMAP_SECURITY_CODE = os.getenv('AMAP_SECURITY_CODE', 'your_amap_security_code')