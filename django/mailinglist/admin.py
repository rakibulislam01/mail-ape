from django.contrib import admin
from .models import MailingList, Message, Subscriber


class MailingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    search_fields = ['id']


admin.site.register(MailingList, MailingListAdmin)
admin.site.register(Message)
admin.site.register(Subscriber)
