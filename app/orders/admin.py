from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(FabricType)
admin.site.register(TailoringStyle)
admin.site.register(OrderBook)
admin.site.register(PricingPlans)
admin.site.register(PricingPlansFabricTyp)
admin.site.register(Measurements)
# admin.site.register(Orders)
admin.site.register(Orders,SimpleHistoryAdmin)