# Generated by Django 4.2.2 on 2023-06-14 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vaultApp', '0002_remove_salt_id_remove_vaultitemmodel_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaultitemmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salt',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='vaultApp.vaultusermodel'),
        ),
        migrations.AlterField(
            model_name='vaultitemmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaultApp.vaultusermodel'),
        ),
        migrations.AlterField(
            model_name='vaultusermodel',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]