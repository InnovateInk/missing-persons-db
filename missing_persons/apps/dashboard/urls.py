from django.urls import include, path

app_name = "dashboard"

urlpatterns = [
    path("", include("missing_persons.apps.dashboard.routes.index")),
    # user urls
    path("users/", include("missing_persons.apps.dashboard.routes.login"))

]
