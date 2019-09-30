from django.contrib import admin
from .models import MailingList, Message, Subscriber


admin.site.register(MailingList)
admin.site.register(Message)
admin.site.register(Subscriber)
