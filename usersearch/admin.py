# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *
from rangevaluesfilterspec import ValueRangeFilter

class GitUserAdmin(admin.ModelAdmin):
        #readonly_fields = ('name_text','live_date','videoId')
        list_display = ('git_id','login','image_tag','email')
        list_filter = ['created',('repos', ValueRangeFilter),('followers', ValueRangeFilter),'location','language','type']
        search_fields =['login','created','email']
        ordering=('-created',)
        def has_add_permission(self, request):
                # Nobody is allowed to add
                return False

        def has_delete_permission(self, request, obj=None):
                # Nobody is allowed to delete
                return False


admin.site.register(GitUser,GitUserAdmin)