from django.urls import path
from .views import getReceipe,ReceipeForm,deleteReceipe,updateReceipe,registerUser,loginUser

urlpatterns=[
    path("receipes",getReceipe),
    path("receipe",ReceipeForm),
    path("register",registerUser),
    path("",loginUser),
    path("deletereceipe/<id>",deleteReceipe,name="delete_receipe"),
    path("updatereceipe/<id>",updateReceipe,name="update_receipe")
]