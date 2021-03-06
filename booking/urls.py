"""URLs for the booking app."""
try:
    from django.conf.urls import patterns, url
except ImportError:  # Pre-Django 1.4 version
    from django.conf.urls.defaults import patterns, url



from . import views


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$',
        views.BookingDetailView.as_view(),
        name='booking_detail'),
    url(r'^create/$',
        views.BookingCreateView.as_view(),
        name='booking_create'),
    url(r'^$', views.BookingListView.as_view(), name='booking_list'),
)
