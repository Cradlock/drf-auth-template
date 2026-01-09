import os
import sys

from django.core.management.base import BaseCommand
from django.conf import settings


# Кастомная команда для запуска uvicorn 
class Command(BaseCommand):

    help = "Запуска джанго в асинхронном-дебаг режиме"

    def add_arguments(self, parser):
        parser.add_argument(
            "--host",
            default="127.0.0.1",
            help="Хост (127.0.0.1) по умолчанию"
        )
        
        parser.add_argument(
            "--port",
            type=int,
            default=8000,
            help="Порт (8000) по умолчанию"
        )

        parser.add_argument(
            "--reload",
            action="store_true",
            help="Включить режим авто-перезагрузки при изменении"
        )



    def handle(self, *args, **options):
        host = options["host"]
        port = options["port"]
        reload = options["reload"]

        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE","core.settings.dev"
        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f"STARTING ASGI server at http://{host}:{port}"
            )
        )

        import uvicorn

        uvicorn.run(
            'core.asgi:application',
            host=host,
            port=port,
            reload=reload,
            log_level="info",
        )



