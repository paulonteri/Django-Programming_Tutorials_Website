from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

from .models import Tutorial

# organize how this model is presented to us.
class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Tutorial,TutorialAdmin)