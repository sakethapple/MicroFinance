from django.contrib import admin
from .models import State
from .models import City
from .models import Customer
from .models import Investor
from .models import Loan_Scheme
from .models import Investment_scheme
from .models import Agent
from .models import Suggetion
# Register your models here.
admin.site.register(State)
admin.site.register(City)
admin.site.register(Customer)
admin.site.register(Investor)
admin.site.register(Agent)
admin.site.register(Loan_Scheme)
admin.site.register(Investment_scheme)
admin.site.register(Suggetion)

