from django.db import models
from django.utils.timezone import now

NULLABLE = {"blank": True, "null": True}

class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Введите заголовок статьи",
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="slug",
        help_text="slug", **NULLABLE
    )
    content = models.TextField(
        verbose_name="Содержание",
        help_text="Введите содержание статьи",
    )
    preview = models.ImageField(
        upload_to="blog/photo",
        verbose_name="Превью",
        help_text="Загрузить превью статьи", **NULLABLE
    )
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата создания", help_text="Укажите дату создания статьи")
    published = models.BooleanField(
        verbose_name="Признак публикации",
        help_text="Укажите признак публикации статьи",
        default=True,
    )
    number_views = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров статьи",
        default=0,
    )

    def __str__(self):
        return f"{self.title} {self.slug} {self.content} {self.preview}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ("title",)
