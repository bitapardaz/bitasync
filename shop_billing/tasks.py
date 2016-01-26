from __future__ import absolute_import

from celery import shared_task

from .bulk_license_generation_modules.generator import generate_bulk_licenses


@shared_task
def generate_license_pdf_files(user_pass_collection):

    generate_bulk_licenses(user_pass_collection)
    return "license pdf files generated"
