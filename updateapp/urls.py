from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.landing,name = 'landingPage'),
    url('^facilities',views.facilities,name = 'facilities'),
    url('^business',views.business,name = 'business'),
    url('^neighborhood',views.neighborhood,name = 'neighborhood'),
    url('^health',views.health,name = 'health'),
    url(r'^police$', views.police, name='police'),
    url(r'^profile/',views.profile,name = 'Profile'),
    url(r'^edit/profile',views.edit_profile,name = 'edit-profile'),
    url(r'^change_profile/(?P<user>\w{0,50})',views.change_profile,name = 'change_profile'),
    url(r'^update/(\d+)',views.update,name ='update'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name ='neighborhood'),
    url(r'^new/update$', views.new_update, name='new-update'),
    url(r'^new/health$', views.new_health, name='new-health'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^search/', views.search, name='search'),
    url(r'^search-detail/(\d+)',views.search_details,name = 'search-detail'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
