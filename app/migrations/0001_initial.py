# Generated by Django 4.2.2 on 2023-07-01 06:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='名前')),
                ('birthday', models.DateField(null=True, verbose_name='生年月日')),
                ('sex', models.CharField(choices=[('男の子', '男の子'), ('女の子', '女の子')], max_length=200, null=True, verbose_name='性別')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='顔写真')),
                ('mated_at', models.DateField(blank=True, null=True, verbose_name='交配日')),
                ('days_to_conceive', models.IntegerField(blank=True, default=63, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='妊娠するまでの日数')),
                ('due_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
