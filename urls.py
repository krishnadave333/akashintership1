from django.conf.urls import url
from todo_list import views


urlpatterns = [
        url('todo_list',views.todo_list),
        url('login_todo' ,views.userlogin),
        url('logout_todo' ,views.userlogout),
        url('add_list',views.add_list),

]
