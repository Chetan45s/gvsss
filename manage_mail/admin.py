from django.contrib import admin
from manage_mail.models import Add_Mail


@admin.register(Add_Mail)
class Add_MailAdmin(admin.ModelAdmin):
    pass
