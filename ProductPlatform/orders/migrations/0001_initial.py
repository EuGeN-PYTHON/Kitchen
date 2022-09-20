# Generated by Django 4.0.4 on 2022-06-23 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название категории')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='category_order/default/placeholder_300x150.png', upload_to='category_order/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Категория заказа',
                'verbose_name_plural': 'Категории заказов',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание заказа')),
                ('status', models.CharField(choices=[('Active', 'Активно'), ('Not Active', 'Не активно')], default='Active', max_length=120, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='ResponseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('offer', models.TextField(verbose_name='Предложение')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
        migrations.CreateModel(
            name='StatusResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('On Approval', 'На согласовании'), ('Approved', 'Утвержден'), ('Not Approved', 'Не утвержден'), ('Cancelled', 'Отменен')], max_length=120, verbose_name='Статус')),
                ('time_status', models.DateTimeField(auto_now_add=True)),
                ('response_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.responseorder', verbose_name='Отклик на заказ')),
            ],
            options={
                'verbose_name': 'Статус отклика',
                'verbose_name_plural': 'Статусы откликов',
            },
        ),
    ]
