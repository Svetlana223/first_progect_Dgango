from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Главная страница была посещена')
    html = """
    <html>
    <head>
        <title>Главная</title>
    </head>
    <body>
        <h1>Добро пожаловать на сайт!</h1>
        <a href="/about/">О себе</a>
    </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    logger.info('Страница "О себе" была посещена')
    html = """
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>lorem100</p>
        <a href="/">На главную</a>
    </body>
    </html>
    """
    return HttpResponse(html)
