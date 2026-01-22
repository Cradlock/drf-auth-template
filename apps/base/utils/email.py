from celery import shared_task 
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.conf import settings 




@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3})
def send_email(template_name, data={}, subject="No Subject", to_email=None):
    """
    Отправка HTML письма через Celery
    
    template_name: путь к шаблону HTML (например "emails/welcome.html")
    data: контекст для шаблона
    subject: тема письма
    to_email: адрес получателя (строка)
    """
    if to_email is None:
        raise ValueError("Поле to_email обязательно")

    # Рендерим HTML-шаблон
    html_content = render_to_string(template_name, data)
    
    # Создаем EmailMultiAlternatives для поддержки HTML и plain text fallback
    email = EmailMultiAlternatives(
        subject=subject,
        body=html_content,  # fallback для plain text
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to_email],
    )
    
    # Добавляем HTML версию письма
    email.attach_alternative(html_content, "text/html")
    
    # Отправляем письмо
    email.send()
    
    return f"Email успешно отправлен на {to_email}"










