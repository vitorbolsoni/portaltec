# Generated by Django 4.1.1 on 2022-11-16 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_aprendizagem', '0014_alter_faqresposta_ds_resposta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vidvideo',
            old_name='qtd_acessos',
            new_name='posicao_video',
        ),
        migrations.AddField(
            model_name='vidassuntovideo',
            name='posicao_assunto',
            field=models.IntegerField(default=0),
        ),
    ]
