# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Store.website'
        db.alter_column(u'store_store', 'website', self.gf('django.db.models.fields.URLField')(max_length=200))
        # Removing index on 'Store', fields ['website']
        db.delete_index(u'store_store', ['website'])


    def backwards(self, orm):
        # Adding index on 'Store', fields ['website']
        db.create_index(u'store_store', ['website'])


        # Changing field 'Store.website'
        db.alter_column(u'store_store', 'website', self.gf('django.db.models.fields.SlugField')(max_length=50))

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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'deal.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'deal.deal': {
            'Meta': {'object_name': 'Deal'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deal.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_ended': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 4, 21, 0, 0)'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 4, 21, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']", 'blank': 'True'}),
            'promo_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'promo_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '250', 'blank': 'True'}),
            'promo_thumbnail': ('django.db.models.fields.URLField', [], {'default': "'media/deal/2013/04/21/19ae6714-bdd5-47be-8099-f1acfcdb986f.jpeg'", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'subcategory_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deal.Subcategory']", 'null': 'True', 'blank': 'True'}),
            'tag_pk': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['deal.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'total_vote': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'})
        },
        u'deal.dealrating': {
            'Meta': {'object_name': 'DealRating'},
            'deal_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deal.Deal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'vote': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'deal.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'category_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deal.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'deal.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'member.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'deal_rating_pk': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['deal.Deal']", 'through': u"orm['deal.DealRating']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landline_1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'landline_2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'store_rating_pk': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['store.Store']", 'through': u"orm['store.StoreRating']", 'symmetrical': 'False'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'store.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'store.store': {
            'Meta': {'object_name': 'Store'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'area_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Area']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'landline_1': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'landline_2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'total_vote': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'store.storerating': {
            'Meta': {'object_name': 'StoreRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Profile']"}),
            'store_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Store']"}),
            'vote': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['store']