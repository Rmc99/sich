from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inscricao.urls', namespace='inscricao')),
    path('', include('usuario.urls', namespace='usuario')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

admin.site.site_header = 'Sistema de Integrado do CH'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Sistema de Integrado do CH'
