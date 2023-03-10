# Generated by Django 4.1.7 on 2023-03-06 20:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('release_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('review', models.CharField(max_length=500)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='images')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.gamer'),
        ),
    ]
