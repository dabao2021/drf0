# Generated by Django 2.2 on 2021-03-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20210309_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_front_iamge',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图'),
        ),
    ]
