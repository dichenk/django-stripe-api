Этот проект реализует бэкенд на Django с интеграцией Stripe API. Он позволяет получать информацию о товарах (Items) и осуществлять покупки через Stripe Checkout. 

## Основные функции

- **Модель Item**: Определяет товары с полями `name`, `description`, `price`.
- **API методы**:
  - `GET /buy/{id}`: Получение Stripe Session Id для оплаты выбранного товара (Item).
  - `GET /item/{id}`: Получение информации о товаре и кнопки для покупки.
- **Stripe Checkout**: Интеграция с Stripe для обработки транзакций.

## Развертывание с использованием Docker

### Конфигурация `docker-compose.yml`

Проект настроен для запуска с использованием `docker-compose`, который включает сервисы `web` (Django приложение) и `nginx` (веб-сервер).

#### Сервис `web`

- Сборка Docker образа Django приложения.
- Определение переменных среды для настройки приложения, включая ключи Stripe и Django secret key.
- Запуск Django приложения с Gunicorn.

#### Сервис `nginx`

- Использование образа Nginx для обслуживания статических файлов и проксирования запросов к Django приложению.
- Проброс порта 8002 для доступа к приложению.

### Запуск проекта

1. Клонируйте репозиторий на ваш сервер.
2. Отредактируйте `docker-compose.yml`, указав ваши значения для переменных среды `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, `DJANGO_SECRET_KEY` и `ALLOWED_HOSTS`.
3. Запустите проект командой:

   ```bash
   docker-compose up -d
   ```

4. Доступ к приложению будет осуществляться через `http://yourserver.com:8002`, где `yourserver.com` - IP-адрес или домен вашего сервера.

### Настройка Nginx

Файл `nginx.conf` должен быть настроен для правильной обработки запросов и обслуживания статических файлов. Убедитесь, что путь к статическим файлам в `nginx.conf` соответствует пути, указанному в `STATIC_ROOT` вашего Django проекта.

## Административная панель Django

Просмотр и управление моделями Django доступны через административную панель Django. Для доступа к ней используйте `/admin` на вашем сайте (например, `http://yourserver.com:8002/admin`).

## Внимание

Проверьте, что вы правильно установили все необходимые ключи и значения в `docker-compose.yml` перед запуском проекта. Для безопасности не используйте дефолтные значения в производственной среде.
