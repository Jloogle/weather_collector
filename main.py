import datetime
import time

from sqlalchemy import select

from database.models import CityWeather, Session, create_table
from settings import CITIES, PERIOD
from utils import get_weather, logger


if __name__ == '__main__':
    create_table()
    with Session() as db_session:
        while True:
            try:
                for city in CITIES:
                    city_weather_data = get_weather(city)
                    city_data = CityWeather(city_weather_data)
                    query_city = select(CityWeather).where(
                        CityWeather.id.__eq__(city_data.id))

                    city_in_base = db_session.execute(query_city).scalar()
                    if not city_in_base:
                        db_session.add(city_data)
                        logger.info(
                            f'Город {city_data.city_name} добавлен в базу'
                        )
                    else:
                        city_in_base.temp = city_data.temp
                        city_in_base.temp_max = city_data.temp_max
                        city_in_base.temp_min = city_data.temp_min
                        city_in_base.date_update = datetime.datetime.now()
                        logger.info(
                            'Обновлены данные для города: '
                            f'{city_in_base.city_name}'
                        )
                    db_session.commit()
                logger.info('Данные успешно обновлены')
            except KeyboardInterrupt:
                logger.info('Программа завершена пользователем')
                db_session.rollback()
                break
            except Exception as e:
                db_session.rollback()
                logger.error(f'Произошла ошибка {e}, завершение программы')
                break
            time.sleep(PERIOD)
