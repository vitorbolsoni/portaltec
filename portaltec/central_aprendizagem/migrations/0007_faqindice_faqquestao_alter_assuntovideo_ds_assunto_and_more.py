# Generated by Django 4.1.1 on 2022-10-08 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('central_aprendizagem', '0006_alter_video_dir_video_alter_video_ds_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqIndice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_indice', models.CharField(max_length=40)),
                ('qtd_acessos', models.IntegerField(default=0)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('grupo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='FaqQuestao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_questao', models.CharField(max_length=100)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('indice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central_aprendizagem.faqindice')),
            ],
        ),
        migrations.AlterField(
            model_name='assuntovideo',
            name='ds_assunto',
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name='FaqResposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_resposta', models.TextField(max_length=500)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central_aprendizagem.faqquestao')),
            ],
        ),
    ]
