from django.contrib import admin
from .models import UserProfile, Mailbox

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender', 'mobile', 'email')

@admin.register(Mailbox)
class MailboxAdmin(admin.ModelAdmin):
    list_display = ('code', 'email', 'type')
