# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'OutgoingSMS.delivery_message'
        db.add_column('mobile_outgoingsms', 'delivery_message', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'IncomingSMS.message_id'
        db.add_column('mobile_incomingsms', 'message_id', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'IncomingMMS.message_id'
        db.add_column('mobile_incomingmms', 'message_id', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'OutgoingSMS.delivery_message'
        db.delete_column('mobile_outgoingsms', 'delivery_message')

        # Deleting field 'IncomingSMS.message_id'
        db.delete_column('mobile_incomingsms', 'message_id')

        # Deleting field 'IncomingMMS.message_id'
        db.delete_column('mobile_incomingmms', 'message_id')


    models = {
        'mobile.incomingmms': {
            'Meta': {'object_name': 'IncomingMMS'},
            'country': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'received_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'mobile.incomingsms': {
            'Meta': {'object_name': 'IncomingSMS'},
            'country': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parameter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'received_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source': ('django.db.models.fields.TextField', [], {})
        },
        'mobile.mmsfile': {
            'Meta': {'object_name': 'MMSFile'},
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mms': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': "orm['mobile.IncomingMMS']"})
        },
        'mobile.outgoingsms': {
            'Meta': {'object_name': 'OutgoingSMS'},
            'country': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '255'}),
            'delivery_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'delivery_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sender': ('django.db.models.fields.CharField', [], {'default': '1212', 'max_length': '255'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mobile']
