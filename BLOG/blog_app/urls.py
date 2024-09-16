from django.urls import path, include
from . import views
from .views import display_topic, post_detail, homepage, AI, AR, cyberSecurity, QuantumComp, Robotics,VR, add_comment
urlpatterns = [
    path('', homepage, name = 'Blog-Home' ),
    path('topics', display_topic ),
    path('AI.html', AI, name = 'Artificial-Intelligence'),
    path('AR.html', AR, name = 'Argumented Reality'),
    path('cyberSecurity.html', cyberSecurity, name = "Cyber Security"),
    path('QuantumComp.html', QuantumComp, name= 'Quantum Computing'),
    path('robotics.html', Robotics, name ="Robotics"),
    path('VR.html', VR, name = 'Virtual Reality' ),
  path('post/<int:post_id>/add_comment/', add_comment, name='add_comment'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]



