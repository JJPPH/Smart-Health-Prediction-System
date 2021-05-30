# Generated by Django 3.2.3 on 2021-05-30 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_patient', '0002_auto_20210530_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pa_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pa_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.IntegerField(default=0)),
                ('sex', models.CharField(choices=[('MAN', 'man'), ('WOMAN', 'woman')], default='MAN', max_length=50)),
                ('personalID', models.CharField(max_length=13)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]