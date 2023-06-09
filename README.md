
# SafeBoard API

Тестовое задание отбора на стажировку Kaspersky, по направлению "Верификация ПО".

# Запуск

Для запуска в репозитории находится скрипт `init.sh`. 

Для запуска скрипта потребуется:

* Включенный docker

* Добавленный user в группу (либо же запуск скрипта с sudo).

Решение проверялось на MacOS на M1, ubuntu 20.04. 

Он собирает docker-image и запускает его.

# Процесс

В качестве процесса, удовлетворяющему условиям был написан скрипт на python, который спустя 10 минут выводит о успешном выполнении процесса.

# Запросы к API

Существует 5 типов запросов:

*  `GET /api/docs`.

*  `POST “start” /api/sleep_process` ("start" является body для запроса).

*  `POST “stop” /api/sleep_process` ("stop" является body для запроса).

*  `GET /api/sleep_process`.

*  `GET /api/sleep_process/result`

# Использование API

Все запросы к API делаются по локальному адресу `0.0.0.0:80`.

Для корректных запросов можно использовать Postman, в случае наличия body у запроса надо проставить его как raw-body (без кавычек).
Либо curl-запросом:
`curl -X POST -X "start/stop" 0.0.0.0:80/<path>`.

Запросы без body, имеют вид: `curl -X GET 0.0.0.0:80/<path>`.