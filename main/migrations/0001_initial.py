# Generated by Django 4.0.5 on 2022-06-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('content', models.CharField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ('-created_at',),
            },
        ),
    ]
