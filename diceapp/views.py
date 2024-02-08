from django.shortcuts import render, HttpResponse
from random import randint, choice
from django.views import View
import logging

LOGGER = logging.getLogger(__name__)


def log(view):
    def wrapper(request, *args, **kwargs):
        res = view(request, *args, **kwargs)
        # print(res.content)
        LOGGER.info(f'The function {view.__name__} was returned {res.content}')
        return res
    return wrapper


@log
def coin(request):
    outcomes = ['орел', 'решка']
    result = choice(outcomes)
    return HttpResponse(result)


@log
def dice(request):
    i = randint(0, 6)
    return HttpResponse(f'Выпало {i}')


@log
def rand_hundred(request):
    i = randint(0, 100)
    return HttpResponse(f'Ваше число: {i}')
