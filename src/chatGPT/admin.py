from django.contrib import admin
from chatGPT.models import User, Chat

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]

class ChatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Chat._meta.fields]

admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)