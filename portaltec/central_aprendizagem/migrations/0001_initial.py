# Generated by Django 4.1.1 on 2022-09-28 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssuntoVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_assunto', models.CharField(max_length=100)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('grupo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_video', models.URLField(max_length=255)),
                ('ds_video', models.CharField(max_length=255)),
                ('qtd_acessos', models.IntegerField(default=0)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('assunto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central_aprendizagem.assuntovideo')),
            ],
        ),
    ]
