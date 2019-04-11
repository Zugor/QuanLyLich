# Generated by Django 2.1.7 on 2019-04-08 06:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonVi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên Đơn Vị')),
            ],
        ),
        migrations.CreateModel(
            name='LichTrinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=256, verbose_name='Nội Dung')),
                ('time_schedule', models.DateTimeField(verbose_name='Thời gian')),
            ],
        ),
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Họ và Tên')),
                ('donvi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.DonVi')),
                ('lichtrinh', models.ManyToManyField(to='App.LichTrinh')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên Đội')),
            ],
        ),
        migrations.AddField(
            model_name='nguoidung',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Team'),
        ),
    ]