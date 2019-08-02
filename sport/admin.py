from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "En tête du site"
admin.site.site_title = "Title"
admin.site.index_title = "Message d'acceuil"
@admin.register(AuthUser)
class UserAdmin(admin.ModelAdmin):#"""information a afficher"""
    list_display = ('username','first_name', 'last_name','email','password') #"""tableau"""
    list_filter = ("date_joined",)
    search_fields = ('is_active', 'is_staff',) #"""champ de recherche"""
    list_per_page = 50 #"""list par page"""

    ordering = ['-is_superuser', '-last_login']

@admin.register(Userprofile)
class UserWebsite(admin.ModelAdmin):
    Userprofile.user.list_display = ('username', 'first_name', 'last_name', 'email', 'password')  # """tableau"""
    Userprofile.user.list_filter = ("date_joined",)
    Userprofile.user.search_fields = ('is_active',)  # """champ de recherche"""
    Userprofile.user.list_per_page = 50  # """list par page"""
    Userprofile.user.ordering = ['-id', '-last_login']

