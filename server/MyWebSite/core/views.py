from django.views.generic.base import TemplateView
from django.conf import settings

class IndexTemplateView(TemplateView):
    def get_template_names(self):
        if not settings.DEBUG:
            template_name = "mainpage/index.html"
        else:
            template_name = "mainpage/index_prod.html"
        return template_name