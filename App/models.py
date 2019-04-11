from django.db import models
from django.contrib import admin
import uuid

# Create your models here.
class Team(models.Model):
    name = models.CharField(verbose_name="Tên Đội", max_length=100)
    def __str__(self):
        return self.name

class DonVi(models.Model):
    name = models.CharField(verbose_name="Tên Đơn Vị", max_length=100)
    def __str__(self):
        return self.name
    class Meta:
         verbose_name_plural = "Đơn Vị"

class LichTrinh(models.Model):
    event = models.CharField(verbose_name="Nội Dung", max_length=256)
    time_schedule = models.DateTimeField(verbose_name="Thời gian")
    def __str__(self):
        return self.event
    class Meta:
         verbose_name_plural = "Lịch Trình"

class LichTrinhAdmin(admin.ModelAdmin):
    list_display = ('event', 'time_schedule')

class NguoiDung(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Họ và Tên", max_length=256)
    team = models.ForeignKey(Team, verbose_name="Tên Đội", on_delete=models.CASCADE)
    donvi = models.ForeignKey(DonVi, verbose_name="Tên Đơn Vị", on_delete=models.CASCADE)
    lichtrinh = models.ManyToManyField(LichTrinh)
    def __str__(self):
        return self.name
    def getData(self):
        return self
    class Meta:
         verbose_name_plural = "Người Dùng"

class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team', 'donvi')
