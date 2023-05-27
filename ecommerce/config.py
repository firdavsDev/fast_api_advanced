import os

APP_ENV = os.environ.get('APP_ENV', 'dev')
# DB Connection
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'postgres')
DATABASE_HOST = os.environ.get('DATABASE_HOST', '172.19.0.2')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'ecommerce')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
# Redis Connection
REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_DB = os.environ.get('REDIS_DB', '0')

TEST_DATABASE_NAME = os.environ.get('TEST_DATABASE_NAME', 'ecommerce_test')
