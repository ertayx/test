from .send_email import send_confirmation_email
from config.celery import app


@app.task()
def send_confirmation_email_task(email, code):
    send_confirmation_email(email, code)
    