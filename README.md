## Схема данных с датчиков
```json
{
    "temperature":"100",
    "humidityAir":"100",
    "humidityDirt": "100",
    "brightnessLevel":"100",
}
```

Для настройки системы нужно создать файл ```.env```.
Используя в качестве примера файл .```env.example```

Для получения данных нужно отправить запрос GET localhost:8080/sensorsData

Для загрузки данных временно можно отправить запрос POST localhost:8080/sensorsData
С телом как у схемы данных

## Запуск проекта

На данный момент для запуска проекта нужно
1. Запустить mongodb
2. git clone https://github.com/lighrik/greenhouse
3. cd greenhouse
4. npm install
5. pip3 install -r requirements.txt
6. npm run serve
7. python3 bot.py


