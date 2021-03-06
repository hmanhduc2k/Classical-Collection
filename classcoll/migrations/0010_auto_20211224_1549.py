# Generated by Django 3.2.6 on 2021-12-24 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classcoll', '0009_auto_20211224_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='group',
        ),
        migrations.AddField(
            model_name='comment',
            name='piece',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='piece', to='classcoll.piece'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='composers',
            field=models.ManyToManyField(blank=True, related_name='composers', to='classcoll.Composer'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='pieces',
            field=models.ManyToManyField(blank=True, related_name='pieces', to='classcoll.Piece'),
        ),
    ]
