from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

from accounts.views import UserRegistrationView
from links.views import NewSubmissionView, SubmissionDetailView, NewCommentView
from links.views import NewCommentReplyView, HomeView, UpvoteSubmissionView
from links.views import RemoveUpvoteFromSubmissionView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^login/$', login, kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': '/login/'}, name='logout'),
    url(r'^register/$', UserRegistrationView.as_view(), name='user-registration'),

    url(r'^new-submission/$', NewSubmissionView.as_view(), name='new-submission'),
    url(r'^submission/(?P<pk>\d+)/$', SubmissionDetailView.as_view(),
        name='submission-detail'),
    url(r'new-comment/$', NewCommentView.as_view(), name='new-comment'),
    url(r'new-comment-reply/$', NewCommentReplyView.as_view(), name='new-comment-reply'),
    url(r'^upvote/(?P<link_pk>\d+)/$', UpvoteSubmissionView.as_view(), name='upvote-submission'),
    url(r'^upvote/(?P<link_pk>\d+)/remove/$', RemoveUpvoteFromSubmissionView.as_view(), name='remove-upvote'),

]
