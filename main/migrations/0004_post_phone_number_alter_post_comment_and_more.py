# Generated by Django 4.1 on 2022-08-28 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_area_alter_post_cur_to_get_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.TextField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cur_to_get',
            field=models.CharField(blank=True, choices=[('Shekel', '₪'), ('Dollar', '$'), ('Euro', '€')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='cur_to_give',
            field=models.CharField(blank=True, choices=[('Shekel', '₪'), ('Dollar', '$'), ('Euro', '€')], max_length=20),
        ),
    ]
