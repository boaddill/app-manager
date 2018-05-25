from django.apps import AppConfig


class InvoicesConfig(AppConfig):
    name = 'apps.invoices'
    def ready(self):
        # signals are imported, so that they are defined and can be used
        import apps.invoices.signals.signals
        import apps.invoices.signals.handlers
