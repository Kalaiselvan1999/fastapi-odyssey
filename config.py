import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_NAME = os.environ.get('DB_NAME')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

SENDER_MAIL_ID = os.environ.get('SENDER_MAIL_ID')
SENDER_MAIL_PASSWORD = os.environ.get('SENDER_MAIL_PASSWORD')
