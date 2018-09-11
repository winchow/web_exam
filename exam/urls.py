from rest_framework import routers
from exam.viewsets import LacViewSet,SubjectViewSet

router = routers.DefaultRouter()
router.register(r'Lac', LacViewSet)
router.register(r'Subject', SubjectViewSet)
