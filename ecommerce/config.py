import os

APP_ENV = os.environ.get('APP_ENV', 'dev')
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'postgres')
DATABASE_HOST = os.environ.get('DATABASE_HOST', '172.20.0.3')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'ecommerce')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
TEST_DATABASE_NAME = os.environ.get('TEST_DATABASE_NAME', 'ecommerce_test')
