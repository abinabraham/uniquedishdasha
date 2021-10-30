from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Branch
from django.contrib.admin import SimpleListFilter
from django.db.models import Q


admin.site.register(Branch)

class UserFilter(SimpleListFilter):
    """
    Filter cls for Members and Non members from \
    App User
    Determining by: Members(user_email != 'pos_only@pos.rh')
    else non members
    """
    title = 'User Roles'
    parameter_name = 'role_name'

    def lookups(self, request, model_admin):
        return [
            ('admin', 'Admin'),
            ('customer', 'Customer'),
            ('staff', 'Staff'),

        ]

    def queryset(self, request, queryset):
        if self.value() == 'admin':
            return queryset.filter(is_superuser=True)
        if self.value() == 'customer':
            return queryset.filter(role_name=2)
        if self.value() == 'staff':
            return queryset.filter(role_name=1)
        

@admin.register(CustomUser)
class AppUserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    search_fields = ('email', 'first_name','last_name',
                     'phone_number')
    list_display = ('first_name','last_name', 'email',
                    'phone_number')
    list_filter = (UserFilter, )
    model = CustomUser
    list_per_page = 30
