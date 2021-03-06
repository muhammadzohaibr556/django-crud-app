# Generated by Django 2.2 on 2020-06-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='post_image/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
