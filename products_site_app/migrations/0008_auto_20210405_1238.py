# Generated by Django 3.1.7 on 2021-04-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_site_app', '0007_auto_20210403_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_products',
            name='picture',
            field=models.ImageField(blank=True, default='default_img.png', null=True, upload_to='static/media/'),
        ),
    ]
