from celery import shared_task

from . import mail


@shared_task
def send_email_task(email: str):
    return mail.order_notification(email)
