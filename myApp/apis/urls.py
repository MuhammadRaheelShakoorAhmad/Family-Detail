from rest_framework import routers
from .viewSets import OfferViewSet, FamilyTypeViewSet, PossibleProgressStatesViewSets, FamilyViewSet

router = routers.SimpleRouter()
router.register('family-type', FamilyTypeViewSet)
router.register('offers', OfferViewSet)
router.register('states', PossibleProgressStatesViewSets)
router.register('family', FamilyViewSet)


urlpatterns = router.urls