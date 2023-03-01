from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('index/', views.index, name='index'),
                  path('login/', views.login_view, name='login'),
                  path('logout/', views.logout_view, name='logout'),
                  path('api/users/', views.users_api, name="users"),
                  path('api/user/<int:id>/', views.user_api, name="user"),
                  path('api/items/', views.items_api, name='items api'),
                  path('api/item/<int:id>/', views.item_api, name='item api'),
                  path('api/bids/', views.bids_api, name='bids api'),
                  path('api/bid/<int:id>/', views.bid_api, name='bid api'),
                  path('api/questions/', views.questions_api, name='questions api'),
                  path('api/question/<int:id>/', views.question_api, name='question api'),
                  path('api/answers/', views.answers_api, name='answers api'),
                  path('api/answer/<int:id>/', views.answer_api, name='answer api'),
                  path('api/uid/', views.get_id, name="uid"),

                  re_path(r'^.*', views.spa_view, name='vue SPA'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns[-1], urlpatterns[-2] = urlpatterns[-2], urlpatterns[-1]
