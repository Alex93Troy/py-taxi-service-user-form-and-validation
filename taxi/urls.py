from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    DriverCreateView,
    DriverDeleteView,
    DriverUpdateView,
    RemoveDriverFromCarView,
    AssignDriverToCarView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer_list",
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer_create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer_update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer_delete",
    ),
    path("cars/", CarListView.as_view(),
         name="car_list"),
    path("cars/<int:pk>/", CarDetailView.as_view(),
         name="car_detail"),
    path("cars/create/", CarCreateView.as_view(),
         name="car_create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(),
         name="car_update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(),
         name="car_delete"),
    path("drivers/", DriverListView.as_view(),
         name="driver_list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(),
         name="driver_detail"),
    path("drivers/create/", DriverCreateView.as_view(),
         name="driver_create"),
    path("drivers/<int:pk>/delete/", DriverDeleteView.as_view(),
         name="driver_delete"),
    path("drivers/<int:pk>/update/", DriverUpdateView.as_view(),
         name="driver_update"),
    path(
        "cars/<int:car_id>/assign-driver/",
        AssignDriverToCarView.as_view(),
        name="assign_driver",
    ),
    path(
        "cars/<int:car_id>/drivers/<int:driver_id>/remove/",
        RemoveDriverFromCarView.as_view(),
        name="remove_driver",
    ),
]

app_name = "taxi"
