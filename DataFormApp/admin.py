from django.contrib import admin

from django.contrib import admin
from .models import Contribution

# Register your models here
@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'contributor_email')
    list_filter = ('contributor_email',)
    search_fields = ('contributor_email',)
