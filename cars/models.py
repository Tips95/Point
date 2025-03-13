from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    year = models.IntegerField(verbose_name="Год выпуска")
    transmission = models.CharField(max_length=20, choices=[('auto', 'Автомат'), ('manual', 'Механика')], verbose_name="КПП")
    engine_volume = models.FloatField(verbose_name="Объем двигателя (л)", default=1.6)
    fuel_consumption = models.FloatField(verbose_name="Средний расход (л/100 км)", default=5.8)
    drive_type = models.CharField(max_length=20, choices=[('front', 'Передний'), ('rear', 'Задний'), ('all', 'Полный')], verbose_name="Привод", default='front')
    rental_schedule = models.CharField(max_length=50, verbose_name="Доступный график аренды", default="5/2, 6/1, 7/0")
    redemption_period = models.CharField(max_length=50, verbose_name="Срок выкупа", default="1, 1.5, 2, 3 года")
    osago = models.CharField(max_length=50, verbose_name="ОСАГО", default="1 год бесплатно")
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за сутки")
    mileage = models.IntegerField(verbose_name="Пробег (км)", default=0)

    def __str__(self):
        return f"{self.name} ({self.year})"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE, verbose_name="Автомобиль")
    image = models.ImageField(upload_to='cars/', verbose_name="Фото")
    is_main = models.BooleanField(default=False, verbose_name="Главное фото")

    def __str__(self):
        return f"Фото для {self.car.name}"

    class Meta:
        verbose_name = "Фото автомобиля"
        verbose_name_plural = "Фото автомобилей"