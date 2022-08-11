from django.contrib import admin
from AmberReq.models import Contact


class AmberAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone', 'created_at', 'updated_at', 'email')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'phone')


admin.site.register(Contact, AmberAdmin)
