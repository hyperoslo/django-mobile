# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OutgoingSMS'
        db.create_table('mobile_outgoingsms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sender', self.gf('django.db.models.fields.CharField')(default=2210, max_length=255)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('country', self.gf('django.db.models.fields.CharField')(default='NO', max_length=255)),
            ('delivery_status', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sent_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mobile', ['OutgoingSMS'])

        # Adding model 'IncomingSMS'
        db.create_table('mobile_incomingsms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('country', self.gf('django.db.models.fields.CharField')(default='NO', max_length=255)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('parameter', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('received_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('source', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mobile', ['IncomingSMS'])

        # Adding model 'IncomingMMS'
        db.create_table('mobile_incomingmms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(default='NO', max_length=255)),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('received_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('source', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mobile', ['IncomingMMS'])

        # Adding model 'MMSFile'
        db.create_table('mobile_mmsfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('mms', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['mobile.IncomingMMS'])),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('mobile', ['MMSFile'])


    def backwards(self, orm):
        
        # Deleting model 'OutgoingSMS'
        db.delete_table('mobile_outgoingsms')

        # Deleting model 'IncomingSMS'
        db.delete_table('mobile_incomingsms')

        # Deleting model 'IncomingMMS'
        db.delete_table('mobile_incomingmms')

        # Deleting model 'MMSFile'
        db.delete_table('mobile_mmsfile')


    models = {
        'mobile.incomingmms': {
            'Meta': {'object_name': 'IncomingMMS'},
            'country': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'received_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mobile.incomingsms': {
            'Meta': {'object_name': 'IncomingSMS'},
            'country': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
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
            'delivery_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sender': ('django.db.models.fields.CharField', [], {'default': '2210', 'max_length': '255'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mobile']
