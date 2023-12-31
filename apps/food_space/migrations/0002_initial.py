# Generated by Django 4.2.3 on 2023-09-20 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food_space', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='food_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_space.foodspace', verbose_name='Место питания'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='food_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_space.foodspace', verbose_name='Место питания'),
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_space.menuitem', verbose_name='Позиция меню'),
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='food_space.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='order',
            name='food_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_space.foodspace', verbose_name='Место питания'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='food_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_space.foodspace', verbose_name='Место питания'),
        ),
        migrations.AddField(
            model_name='image',
            name='food_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='food_space.foodspace'),
        ),
        migrations.AddField(
            model_name='event',
            name='food_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_space.foodspace', verbose_name='Место питания'),
        ),
    ]
