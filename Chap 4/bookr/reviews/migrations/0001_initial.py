# Generated by Django 4.0.3 on 2022-03-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the Publisher.', max_length=50)),
                ('website', models.URLField(help_text="The Publisher's website")),
                ('email', models.EmailField(help_text="The Publisher's email adress", max_length=254)),
            ],
        ),
    ]
