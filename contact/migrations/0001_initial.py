# Generated by Django 2.0.8 on 2018-09-17 08:47

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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Email_Address', models.EmailField(max_length=254)),
                ('Phone_Number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9848012345'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Contact_Number', models.CharField(max_length=10)),
                ('Category', models.CharField(choices=[('dev', 'Developer'), ('rep', 'Reporter'), ('manager', 'Manager')], default='Developer', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
