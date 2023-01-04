# Generated by Django 4.0.1 on 2022-01-17 04:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EoElection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('credential_period_from', models.DateTimeField()),
                ('credential_period_to', models.DateTimeField()),
                ('casting_period_from', models.DateTimeField()),
                ('casting_period_to', models.DateTimeField()),
                ('tallying_period', models.DateTimeField()),
                ('voter_list', models.FileField(upload_to='')),
                ('candidates_list', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='EoVoterUser',
            fields=[
                ('userid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('public_key', models.CharField(max_length=255)),
                ('eo_election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eovote.eoelection')),
            ],
        ),
    ]