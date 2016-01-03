from __future__ import absolute_import

from celery import shared_task
from .bulk_license_generation_modules.generator import generate_bulk_licenses


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def generator_bulk_licenses_task(user_pass_collection):

    user_pass_collection=[('ali','testali'),('hamid','testhamid'),('mozi','testmozi'),('reza','testreza'),('soosan','testsoosan'),('jamshid','testjamshid')]
    generate_bulk_licenses(user_pass_collection)


    return "write to file done"
    #generate_bulk_licenses(user_pass_collection)
