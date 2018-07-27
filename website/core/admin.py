from django.contrib import admin

# Register your models here.
from website.core.models import New, Channel, Sugestao

admin.site.register(Channel)
admin.site.register(New)
admin.site.register(Sugestao)