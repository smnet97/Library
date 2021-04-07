from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet)
router.register(r'lib-users', views.LibUserViewSet)
router.register(r'renter-books', views.RentBookViewSet)
