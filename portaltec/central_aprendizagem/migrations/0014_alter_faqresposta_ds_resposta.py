# Generated by Django 4.1.2 on 2022-11-09 13:40

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('central_aprendizagem', '0013_alter_faqresposta_ds_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqresposta',
            name='ds_resposta',
            field=tinymce.models.HTMLField(max_length=2200),
        ),
    ]
