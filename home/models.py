from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    templates="home/home_page.html"
    max_count=1 #limit the number of home page#
    # content_title = models.CharField(max_length=500,blank=False,null=True)
    # content_subtitle = RichTextField(features=["bold","italic"],null=True)
    # content_panels = Page.content_panels + [
    #     FieldPanel("content_title"),
    #     FieldPanel("content_subtitle"),
    # ]

class Meta:
    verbose_name="Home Page"
    verbose_name_plural="Home Pages"