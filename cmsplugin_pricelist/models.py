from django.db import models
from cms.models import CMSPlugin
from filer.fields.folder import FilerFolderField
from cms.plugin_pool import plugin_pool
from djangocms_text_ckeditor.widgets import TextEditorWidget
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField

class PriceSubItem(models.Model):
	ps_title = models.CharField(_("Title"), max_length=100)
	ps_imgsrc = models.ImageField(_("Image"), upload_to='pricelist/subitems',blank=True)
	ps_content = HTMLField(_('Content'), configuration="CKEDITOR_SETTINGS_MODEL1",blank=True)
	
	def __unicode__(self):
		return self.ps_title


class PriceItem(models.Model):
	pi_title = models.CharField(_("Title"), max_length=100) 
	cars = models.ManyToManyField(PriceSubItem,verbose_name=_("Cars"),blank=True)

	def __unicode__(self):
		return self.pi_title

class Pricelist(CMSPlugin):
	the_title = models.CharField(_("Title"), max_length=100,blank=True)
	imgsrc = models.ImageField(_("Image"), upload_to='pricelist/',blank=True)
	content = HTMLField(_('Content'), configuration="CKEDITOR_SETTINGS_MODEL1",blank=True)
	the_gallery = FilerFolderField(verbose_name=_('Gallery'),blank=True)
	choices = models.ManyToManyField(PriceItem,verbose_name=_("Choose objects"),blank=True)
	
	def __unicode__(self):
		return self.the_title
	
	@property
	def images(self):
		if not hasattr(self, '__images'):
			files = self.the_gallery.files
			self.__images = [f for f in files if f.file_type == 'Image']
			self.__images.sort()
		return self.__images