from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Pricelist, PriceItem
from django.utils.translation import ugettext as _
from django.contrib import admin

class CMSPricelistPlugin(CMSPluginBase):
	model = Pricelist
	name = _("Pricelist")
	render_template = "cmsplugin_pricelist/template.html"
	
	
	def render(self, context, instance, placeholder):
		pricelists = Pricelist.objects.all()
		priceitems = PriceItem.objects.all()
		context.update({
				'Pricelist': instance,
				'images': instance.images,
				'pricelists': pricelists,
				'priceitems': priceitems,
					})
		return context


plugin_pool.register_plugin(CMSPricelistPlugin)