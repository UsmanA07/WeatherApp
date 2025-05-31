## WeatherApp

Простое DRF-приложение для просмотра прогноза погоды по названию города с рядом дополнительных возможностей.

### Что реализовано

- Получение прогноза погоды по названию города (OpenMeteo API)

- Удобный формат вывода погоды (текущая + прогноз на несколько часов)

- Автодополнение (подсказки) при вводе города (через Nominatim API)

- Сохранение последнего введённого города в cookies

- API со статистикой: сколько раз и какие города запрашивались

### Технологии

- Python 3.13

- Poetry - управление зависимостями и запуск

- Django 5 + Django REST Framework

- httpx - запросы к внешним API

- PostgreSQL - основная БД

- Docker - заготовка под контейнеризацию

---

### Установка и запуск

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/UsmanA07/drf-social-network.git
   cd drf-social-network
   ```

2. Запустите docker и создайте superuser

   ```bash
    docker-compose up --build
    sudo docker exec -it weatherapp-backend-1 python src/manage.py createsuperuser
    ```

---

### Эндпоинты

- **GET** `/api/weather/?city=Berlin` - Прогноз погоды
- **GET** `/api/weather/` - Прогноз по последнему городу из куки
- **GET** `/api/weather/autocomplete/` - Подсказки по вводу города (?query=...)