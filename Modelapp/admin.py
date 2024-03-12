from django.contrib import admin

from .models import Docters
from .models import Parents
from .models import Students
from .models import Teachers
from .models import Post

admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Docters)
admin.site.register(Parents)
admin.site.register(Post)
