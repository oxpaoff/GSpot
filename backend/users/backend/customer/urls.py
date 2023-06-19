from django.urls import path
from rest_framework.routers import DefaultRouter

from customer.views.v1.auth_view import CustomerAuthView
from customer.views.v1 import account_views
from customer.views.v1.customer_friend_view import AddFriendsView
from customer.views.v1.customer_registration_view import CustomerRegistrationView
from customer.views.v1 import customer_friend_view

urlpatterns = [
    path("registration/", CustomerRegistrationView.as_view()),
]

account_router = [
    path(
        "customer/me",
        account_views.AccountViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
        name="customer-user-account",
    ),
    path(
        "customer/me/change-password",
        account_views.ChangePasswordViewSet.as_view({"post": "create"}),
        name="customer-user-change-password",
    ),
]

auth_routes = [path("login/", CustomerAuthView.as_view(), name="customer_login")]

friends = [
    path('customers/', AddFriendsView.as_view({'get': 'list'}), name='customers-list'),
    path(
        'customers/<uuid:user_id>/',
        AddFriendsView.as_view({'get': 'retrieve'}),
        name='customers-detail',
    ),
    path(
        'customers/<uuid:user_id>/add-friends/',
        AddFriendsView.as_view({'post': 'add_friend'}),
        name='customers-add_friend',
    ),
    path(
        'friends_requests/',
        customer_friend_view.GetListAcceptAddFriendsView.as_view(),
        name='list-friends-requests',
    ),
    path(
        'friends_requests/<uuid:user_id>/ ',
        customer_friend_view.RetrieveAcceptRejectAddFriendsView.as_view(
            {'get': 'retrieve', 'post': 'create', 'delete': 'destroy'}
        ),
        name='retrieve-accept-reject-friend',
    ),
    path(
        'friends/',
        customer_friend_view.GetAllFriendsView.as_view(),
        name='my-friends',
    ),
    path(
        'friends/<uuid:user_id>/',
        customer_friend_view.RetrieveDestroyFriendsView.as_view(),
        name='retrieve-destroy-friend',
    ),
]


urlpatterns += account_router
urlpatterns += auth_routes
urlpatterns += friends
