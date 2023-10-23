import os

from dotenv import load_dotenv


load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='postgres')
DB_HOST = os.getenv('DB_HOST', default='postgres')
DB_NAME = os.getenv('DB_NAME', default='postgres')
DB_PORT = os.getenv('DB_PORT', default='5432')
DB_PATH = (
    'postgresql+psycopg2://'
    f'{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
API_KEY = os.getenv('API_KEY')

PERIOD = 3600


CITIES = [
    'Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mexico City', 'Cairo',
    'Mumbai', 'Beijing', 'Dhaka', 'Osaka', 'New York', 'Karachi',
    'Buenos Aires', 'Chongqing', 'Istanbul', 'Kolkata', 'Manila', 'Lagos',
    'Rio de Janeiro', 'Tianjin', 'Kinshasa', 'Guangzhou', 'Los Angeles',
    'Moscow', 'Shenzhen', 'Lahore', 'Bangalore', 'Paris', 'Bogotá', 'Jakarta',
    'Chennai', 'Lima', 'Bangkok', 'Seoul', 'Nagoya', 'Hyderabad', 'London',
    'Tehran', 'Chicago', 'Chengdu', 'Nanjing', 'Wuhan', 'Ho Chi Minh City',
    'Luanda', 'Ahmedabad', 'Kuala Lumpur', 'Hong Kong', 'Dongguan', 'Foshan',
    'Hangzhou'
]
