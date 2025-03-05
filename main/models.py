from django.db import models


class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    contact_info = models.TextField(verbose_name="Контактная информация")
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото")
    services = models.ManyToManyField(
        "Service", verbose_name="Услуги", related_name="masters"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    master = models.ManyToManyField(
        Master, verbose_name="Мастер", related_name="service"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Visit(models.Model):
    STATUS_CHOICES = [
        (0, "Создана"),
        (1, "Подтверждена"),
        (2, "Отменена"),
        (3, "Выполнена"),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=0, verbose_name="Статус"
    )
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    services = models.ManyToManyField(Service, verbose_name="Услуги")

    def __str__(self):
        return f"{self.name} ({self.phone}) -> {self.services}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
