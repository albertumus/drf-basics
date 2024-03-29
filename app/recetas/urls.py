from django.conf.urls import url
from django.urls import path

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.urlpatterns import apply_suffix_patterns

from recetas.views import *

app_name = "recetas"

recetas_router = DefaultRouter()
recetas_router.register( r'recetas', RecetasViewSet, basename="recetas"  )
recetas_router.register( r'recetashtml', RecetasViewSetHTML, basename="recetas_html" )

recetas_simple_router = SimpleRouter() 
recetas_simple_router.register( r'ingredientesprivate', IngredientesPrivateViewSet, basename="ingredientesprivate"  )
recetas_simple_router.register( r'ingredientespublic', IngredientesPublicViewSet, basename="ingredientespublic"  )

urlpatterns = [

    url( r"^tiporeceta/$", API_get_tipo_recetas, name="recetas_tiporeceta_list" ),
    url( r"^ingredientes/$", IngredientesView.as_view(), name="ingredientes" ),
    url( r"^ingredientes/(?P<pk>[0-9]+)/delete$", IngredienteDeleteView.as_view(), name="ingredientes_delete" ),

    # Deseos
    url( r'^deseos/$', DeseoListAPIView.as_view(), name="deseos_list" ),
    url( r'^deseos/(?P<pk>[0-9]+)/$', SwitchDeseo, name="deseos_switch"),
]

urlpatterns += recetas_router.urls
urlpatterns += recetas_simple_router.urls

