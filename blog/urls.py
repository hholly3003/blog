from django.urls import path
from blog import views

urlpatterns = [
    path('',view.PostListView.as_view(),name='post_list'),
    path('about',views.AboutView.as_view(),name='about'),
    path('post/<pk>',view.PostDetailView.as_view(),name='post_detail'),
    path('post/new',view.PostCreateView.as_view(),name='post_new'),
    path('post/<pk>/edit',view.PostUpdateView.as_view(),name='post_edit'),
    path('post/<pk>/remove',view.PostDeleteView.as_view(),name='post_remove'),
    path('drafts',view.DraftListView.as_view(),name='post_draft_list')
]
