from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    # ネコの情報 #
    CHOICES = [
        ('男の子', '男の子'),
        ('女の子', '女の子'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name="名前", max_length=200, null=True)
    birthday = models.DateField(verbose_name="生年月日", null=True)
    sex = models.CharField(verbose_name="性別", max_length=200, choices=CHOICES, null=True)
    image = models.ImageField(upload_to='images', verbose_name="顔写真", null=True, blank=True)
    mated_at = models.DateField(verbose_name="交配日", blank=True, null=True)
    days_to_conceive = models.IntegerField(verbose_name="妊娠するまでの日数", null=True, blank=True, default=63, validators=[MinValueValidator(1), MaxValueValidator(100)])
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField("作成日", default=timezone.now)
    updated_at = models.DateTimeField("更新日", default=timezone.now)

    def save(self, *args, **kwargs):
        if self.mated_at:
            if not self.days_to_conceive:
                self.days_to_conceive = 63
            self.due_date = self.mated_at + timedelta(days=self.days_to_conceive)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name