from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()
class Advertisements(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField("изображение", upload_to="advertisments",default = None)
    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html("<span style='color:green; font-weight:bold'>Сегодня в {}</span>", created_time)
        return self.created_at.strftime("%d:%m:%Y в %H:%M:%S")

    @admin.display(description="дата обновления")
    def created_update(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            created_time_2 = self.updated_at.time().strftime("%H:%M:%S")
            return format_html("<span style='color:yellow; font-weight:bold'>Сегодня в {}</span>", created_time_2)
        return self.created_at.strftime("%d:%m:%Y в %H:%M:%S")
    class Meta:
            db_table = "advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"