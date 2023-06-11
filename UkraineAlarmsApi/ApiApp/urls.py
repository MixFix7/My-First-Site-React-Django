from rest_framework import routers
from .api import UkraineViewSet

router = routers.DefaultRouter()
router.register('api/ukrainealarms', UkraineViewSet, 'Ukraine')

urlpatterns = router.urls
