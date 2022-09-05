from django.contrib import admin
from .models import employee
from .models import electrician
from .models import plumber
from .models import AC_service
from .models import TV_service
from .models import carpenter
from .models import house_keeper
from .models import renovator
# Register your models here.
admin.site.register(employee)
admin.site.register(electrician)
admin.site.register(plumber)
admin.site.register(AC_service)
admin.site.register(TV_service)
admin.site.register(carpenter)
admin.site.register(house_keeper)
admin.site.register(renovator)
