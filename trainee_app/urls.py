from django.urls import path
from .views import TraineeListView, TraineeDetailView, TraineeDeleteView, AddTrainee, UpdateTrainee, register

urlpatterns = [
    path("", TraineeListView.as_view(), name="trainee_list"),
    path("add/", AddTrainee.as_view(), name="add_trainee"),
    path("trainee/<int:pk>/", TraineeDetailView.as_view(), name="trainee_detail"),
    path("update/<int:trainee_id>/", UpdateTrainee.as_view(), name="update_trainee"),
    path("trainee/<int:pk>/delete/", TraineeDeleteView.as_view(), name="delete_trainee"),
    path('register/', register, name='register'),
]
