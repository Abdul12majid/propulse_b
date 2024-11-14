from django.contrib import admin
from .models import Utility, HostelMedia, Hostel, Message

# Register your models here.

admin.site.register(Utility)
admin.site.register(HostelMedia)
admin.site.register(Hostel)
admin.site.register(Message)