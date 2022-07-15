from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from tracker.views import HomeView, UserSignupView, ExerciseCreateView, ExerciseListView, ExerciseDetailView, ExerciseUpdateView, ExerciseDeleteView

app_name = "tracker"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('signup', UserSignupView.as_view(), name="signup"),
    path(
        "create/",
        login_required(ExerciseCreateView.as_view()),
        name="exercise_create"),
    path(
        "all/",
        ExerciseListView.as_view(),
        name="exercise_list"),
    path(
        "<int:pk>/",
        ExerciseDetailView.as_view(),
        name="exercise_detail"
        ),
    path(
        "<int:pk>/update/",
        login_required(ExerciseUpdateView.as_view()),
        name="exercise_update"),
    path(
        "<int:pk>/delete/",
        login_required(ExerciseDeleteView.as_view()),
        name="exercise_delete"),
]