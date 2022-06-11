# Generated by Django 3.1.2 on 2021-10-31 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='doc_path',
            field=models.CharField(default='Documents', max_length=200),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]