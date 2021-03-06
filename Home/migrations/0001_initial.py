# Generated by Django 2.0.1 on 2018-02-16 08:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('code', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='')),
                ('notifications', models.CharField(max_length=1000000)),
                ('error', models.CharField(max_length=1000000)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('state', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=100)),
                ('imgf', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PetCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PetCategoryKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.PetCategory')),
            ],
        ),
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.PetCategory'),
        ),
        migrations.AddField(
            model_name='pet',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.PetCategoryKind'),
        ),
    ]
