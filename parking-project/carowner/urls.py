from django.urls import path , include

from carowner.views import CarOwnerCreate, CarOwnerDetail, CarOwnerUpdate, CarOwnerDelete, CarOwnerList


urlpatterns = [
    path('create/', CarOwnerCreate.as_view()),
    path('', CarOwnerList.as_view()),
    path('<int:pk>/', CarOwnerDetail.as_view()),
    path('update/<int:pk>/', CarOwnerUpdate.as_view()),
    path('delete/<int:pk>/', CarOwnerDelete.as_view()),
]