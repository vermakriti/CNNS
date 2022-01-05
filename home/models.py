from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    templates="home/home_page.html"
    max_count=1 #limit the number of home page#
    

class Meta:
    verbose_name="Home Page"
    verbose_name_plural="Home Pages"

