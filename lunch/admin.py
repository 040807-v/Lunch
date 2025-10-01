from django.contrib import admin
from .models import Pedido, Refeicao, UserProfile

admin.site.register(Pedido)
admin.site.register(Refeicao)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'isStaff')
    list_editable = ('isStaff',)