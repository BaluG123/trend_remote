# Generated by Django 3.2.3 on 2021-10-10 09:40

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('testapp', '0003_alter_trends_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mimage', models.FileField(blank=True, null=True, upload_to='images/')),
                ('caption', models.CharField(blank=True, max_length=28, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
