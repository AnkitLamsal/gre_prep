from django.contrib import admin
from .models import Family, Word, WordFamily

# Register your models here.
admin.site.register(Family)
admin.site.register(Word)
admin.site.register(WordFamily)