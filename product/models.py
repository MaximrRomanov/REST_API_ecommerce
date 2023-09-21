from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название категории", unique=True
    )
    slug = models.SlugField(max_length=100, verbose_name="Слаг", unique=True)
    description = models.TextField(
        max_length=255, verbose_name="Описание категории", blank=True
    )
    # TODO: ДОБАВИТЬ ОТДЕЛЬНУЮ ТАБЛИЦУ ДЛЯ cat_image
    # cat_image = models.ImageField(upload_to="photos/categories", blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    class StatusType(models.TextChoices):
        AVAILABLE = "AV", "Доступен"
        UNAVAILABLE = "UV", "Недоступен"

    status = models.CharField(
        verbose_name="Статус продукта",
        max_length=2,
        choices=StatusType.choices,
        default=StatusType.AVAILABLE,
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория товара", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=200, verbose_name="Название продукта", unique=True
    )
    slug = models.SlugField(max_length=200, verbose_name="Слаг", unique=True)
    description = models.TextField(
        max_length=500, verbose_name="Описание продукта", blank=True
    )
    weight = models.CharField(verbose_name="Вес", blank=True, null=True, max_length=255)
    model = models.CharField(
        verbose_name="Модель", max_length=255, blank=True, null=True
    )
    vendor = models.CharField(
        verbose_name="Производитель", max_length=255, blank=True, null=True
    )
    url = models.URLField(
        verbose_name="Ссылка на оригинальный товар", blank=True, null=True
    )
    price = models.PositiveBigIntegerField(verbose_name="Актуальная цена продукта")
    old_price = models.PositiveBigIntegerField(
        verbose_name="Старая цена продукта", blank=True, null=True
    )
    # TODO: ДОБАВИТЬ ОТДЕЛЬНУЮ ТАБЛИЦУ ДЛЯ product_image
    # images = models.ImageField(upload_to="photos/products")
    count = models.PositiveBigIntegerField(
        verbose_name="Количество продукта", default=0
    )

    # on_delete=models.CASCADE говорит, что когда удаляяем категорию, удаляются все товары этой категорию

    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def set_available(self):
        """
        Метод, который меняет статус на Доступен

        """
        self.status = Product.StatusType.AVAILABLE
        self.save()

    def set_unavailable(self):
        """
        Метод, который меняет статус на Недоступен

        """
        self.status = Product.StatusType.UNAVAILABLE
        self.save()

    def __str__(self):
        return self.name
