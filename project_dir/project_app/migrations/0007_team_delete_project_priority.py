# Generated by Django 4.2 on 2023-04-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0006_project_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('t_name', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='project_priority',
        ),
    ]
