from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from todo.views import all_todos, add_todo, remove_todo, edit_todo, register_user, login_user, online_users, share_todo

schema_view = get_schema_view(
    openapi.Info(
        title="Todo list",
        default_version='v1',
        description="Todo list",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="creudnitsky200206@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('all-todos/<str:profile_id>', all_todos),
    path('add-todo/<str:profile_id>', add_todo),
    path('edit-todo/<str:identifier>', edit_todo, name='edit_todo'),
    path('delete-todo/<str:identifier>', remove_todo, name='remove_todo'),
    path('share-todo/<str:profile_id>', share_todo),
    path('auth/register/', register_user),
    path('auth/login/', login_user),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('online_users/', online_users, name='online_users'),
]

