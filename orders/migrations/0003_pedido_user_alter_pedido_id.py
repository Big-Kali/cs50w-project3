# Generated by Django 4.0.5 on 2022-06-12 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='user',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]