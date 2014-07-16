from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from django.contrib import admin
import models
from models import PriceItem
from models import PriceSubItem

class PriceItemInlineAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
	model = models.PriceItem
	list_display = ('pi_title',)
	
class PriceSubItemInlineAdmin(admin.ModelAdmin):
	model = models.PriceSubItem
	list_display = ('ps_title',)
	
admin.site.register(PriceItem, PriceItemInlineAdmin)
admin.site.register(PriceSubItem, PriceSubItemInlineAdmin)