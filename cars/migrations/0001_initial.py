# Generated by Django 4.2.19 on 2025-03-03 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('transmission', models.CharField(choices=[('auto', 'Автомат'), ('manual', 'Механика')], max_length=20, verbose_name='КПП')),
                ('engine_volume', models.FloatField(default=1.6, verbose_name='Объем двигателя (л)')),
                ('fuel_consumption', models.FloatField(default=5.8, verbose_name='Средний расход (л/100 км)')),
                ('drive_type', models.CharField(choices=[('front', 'Передний'), ('rear', 'Задний'), ('all', 'Полный')], default='front', max_length=20, verbose_name='Привод')),
                ('rental_schedule', models.CharField(default='5/2, 6/1, 7/0', max_length=50, verbose_name='Доступный график аренды')),
                ('redemption_period', models.CharField(default='1, 1.5, 2, 3 года', max_length=50, verbose_name='Срок выкупа')),
                ('osago', models.CharField(default='1 год бесплатно', max_length=50, verbose_name='ОСАГО')),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за сутки')),
                ('mileage', models.IntegerField(default=0, verbose_name='Пробег (км)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='RentalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('driving_experience', models.CharField(max_length=50, verbose_name='Водительский стаж с')),
                ('license_number', models.CharField(max_length=20, verbose_name='Серия и номер ВУ')),
                ('license_country', models.CharField(max_length=100, verbose_name='Страна выдачи ВУ')),
                ('license_issue_date', models.DateField(verbose_name='Дата выдачи ВУ')),
                ('license_expiry_date', models.DateField(verbose_name='Действует до')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='Автомобиль')),
            ],
            options={
                'verbose_name': 'Заявка на аренду',
                'verbose_name_plural': 'Заявки на аренду',
            },
        ),
    ]
