from django.apps import AppConfig


class ScrapingConfig(AppConfig):
    name = 'scraping'
    verbose_name = 'Приложение по сботу вакансий: Scraping'
    # так же надо переопределить __init__
