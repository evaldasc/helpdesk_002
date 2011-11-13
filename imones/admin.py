from django.contrib import admin
from helpdesk_002.imones.models import Company, Branch, UserProfile


admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(UserProfile)
