# Generated by Django 4.1.1 on 2022-10-08 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_aprendizagem', '0010_rename_qtd_acessos_faqindice_numero_indice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faqindice',
            old_name='numero_indice',
            new_name='posicao_indice',
        ),
        migrations.AddField(
            model_name='faqquestao',
            name='posicao_questao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='faqresposta',
            name='posicao_resposta',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faqresposta',
            name='ds_resposta',
            field=models.TextField(max_length=999),
        ),
    ]
