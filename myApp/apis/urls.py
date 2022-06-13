from rest_framework import routers
from .viewSets import OfferViewSet, FamilyTypeViewSet, PossibleProgressStatesViewSets

router = routers.SimpleRouter()
router.register('family', FamilyTypeViewSet)
router.register('offers', OfferViewSet)
router.register('states', PossibleProgressStatesViewSets)



urlpatterns = router.urls