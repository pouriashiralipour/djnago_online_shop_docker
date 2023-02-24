from django.urls import path

urlpatterns = [
    path('signup/', SignUpView.asView(), name='sign_up'),
]
