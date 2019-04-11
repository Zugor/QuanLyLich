from django.contrib import admin

from .models import Team, DonVi, LichTrinh, LichTrinhAdmin, NguoiDung, NguoiDungAdmin

admin.site.register(Team)
admin.site.register(DonVi)
admin.site.register(LichTrinh, LichTrinhAdmin)
admin.site.register(NguoiDung, NguoiDungAdmin)