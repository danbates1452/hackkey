# Generated by Django 4.2.10 on 2024-02-18 01:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('logged_in_today', models.BooleanField(default=True)),
                ('login_daily_claimed', models.BooleanField(default=False)),
                ('selected_theme', models.CharField(choices=[('dark', 'Dark'), ('light', 'Light'), ('blue', 'Blue'), ('lightblue', 'Light Blue'), ('grey', 'Grey'), ('green', 'Green'), ('red', 'Red'), ('yellow', 'Yellow')], default='dark', max_length=9)),
                ('rolls_owned', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='PremiumFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enhanced_password_generation', models.BooleanField(verbose_name='Enhanced Password Generation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackkey.users')),
            ],
        ),
        migrations.CreateModel(
            name='GachaRewards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dark_theme', models.BooleanField(default=False, verbose_name='Dark Theme')),
                ('light_theme', models.BooleanField(default=False, verbose_name='Light Theme')),
                ('blue_theme', models.BooleanField(default=False, verbose_name='Blue Theme')),
                ('lightblue_theme', models.BooleanField(default=False, verbose_name='Light Blue Theme')),
                ('grey_theme', models.BooleanField(default=False, verbose_name='Grey Theme')),
                ('green_theme', models.BooleanField(default=False, verbose_name='Green Theme')),
                ('red_theme', models.BooleanField(default=False, verbose_name='Red Theme')),
                ('yellow_theme', models.BooleanField(default=False, verbose_name='Yellow Theme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackkey.users')),
            ],
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('uri', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackkey.users')),
            ],
        ),
    ]
