"""djangoLearningSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# From The Net Ninja Tutorial # 12
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from polls.views import results, detail, vote, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]

# From The Net Ninja Tutorial # 12
urlpatterns += staticfiles_urlpatterns()
"""
The include() function allows referencing other URLconfs. 
Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point 
and sends the remaining string to the included URLconf for further processing.
So when I view polls.url those path fuctions will refer to the path under polls
But won't include the actuals polls part of the URL path

You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.
"""