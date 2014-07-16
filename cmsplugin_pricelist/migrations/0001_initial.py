# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PriceSubItem'
        db.create_table(u'cmsplugin_pricelist_pricesubitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ps_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ps_imgsrc', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('ps_content', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_pricelist', ['PriceSubItem'])

        # Adding model 'PriceItem'
        db.create_table(u'cmsplugin_pricelist_priceitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pi_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'cmsplugin_pricelist', ['PriceItem'])

        # Adding M2M table for field cars on 'PriceItem'
        m2m_table_name = db.shorten_name(u'cmsplugin_pricelist_priceitem_cars')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('priceitem', models.ForeignKey(orm[u'cmsplugin_pricelist.priceitem'], null=False)),
            ('pricesubitem', models.ForeignKey(orm[u'cmsplugin_pricelist.pricesubitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['priceitem_id', 'pricesubitem_id'])

        # Adding model 'Pricelist'
        db.create_table(u'cmsplugin_pricelist_pricelist', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('the_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('imgsrc', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('content', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('the_gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Folder'], blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_pricelist', ['Pricelist'])

        # Adding M2M table for field choices on 'Pricelist'
        m2m_table_name = db.shorten_name(u'cmsplugin_pricelist_pricelist_choices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pricelist', models.ForeignKey(orm[u'cmsplugin_pricelist.pricelist'], null=False)),
            ('priceitem', models.ForeignKey(orm[u'cmsplugin_pricelist.priceitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pricelist_id', 'priceitem_id'])


    def backwards(self, orm):
        # Deleting model 'PriceSubItem'
        db.delete_table(u'cmsplugin_pricelist_pricesubitem')

        # Deleting model 'PriceItem'
        db.delete_table(u'cmsplugin_pricelist_priceitem')

        # Removing M2M table for field cars on 'PriceItem'
        db.delete_table(db.shorten_name(u'cmsplugin_pricelist_priceitem_cars'))

        # Deleting model 'Pricelist'
        db.delete_table(u'cmsplugin_pricelist_pricelist')

        # Removing M2M table for field choices on 'Pricelist'
        db.delete_table(db.shorten_name(u'cmsplugin_pricelist_pricelist_choices'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_pricelist.priceitem': {
            'Meta': {'object_name': 'PriceItem'},
            'cars': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmsplugin_pricelist.PriceSubItem']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pi_title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cmsplugin_pricelist.pricelist': {
            'Meta': {'object_name': 'Pricelist', '_ormbases': ['cms.CMSPlugin']},
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cmsplugin_pricelist.PriceItem']", 'symmetrical': 'False', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'imgsrc': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'the_gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['filer.Folder']", 'blank': 'True'}),
            'the_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'cmsplugin_pricelist.pricesubitem': {
            'Meta': {'object_name': 'PriceSubItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ps_content': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'ps_imgsrc': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'ps_title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'filer.folder': {
            'Meta': {'ordering': "(u'name',)", 'unique_together': "((u'parent', u'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['filer.Folder']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_pricelist']