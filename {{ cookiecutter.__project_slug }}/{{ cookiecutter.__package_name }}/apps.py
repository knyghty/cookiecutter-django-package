from django.apps import AppConfig


class {{ cookiecutter.__app_class }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.__package_name }}"
    label = "{{ cookiecutter.__app_label }}"
