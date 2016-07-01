from django.conf.urls import patterns, url, include
from api import views

person_list = views.PersonViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

person_detail = views.PersonViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

courseresult_list = views.CourseresultViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

courseresult_detail = views.CourseresultViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

building_list = views.BuildingViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

building_detail = views.BuildingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

testresult_list = views.TestresultViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

testresult_detail = views.TestresultViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

course_list = views.CourseViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

course_detail = views.CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

schedule_list = views.ScheduleViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

schedule_detail = views.ScheduleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

room_list = views.RoomViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

room_detail = views.RoomViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

group_list = views.GroupViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

group_detail = views.GroupViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

grouprole_list = views.GrouproleViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

grouprole_detail = views.GrouproleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

newsfeed_list = views.NewsfeedViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

newsfeed_detail = views.NewsfeedViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

newsitem_list = views.NewsitemViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

newsitem_detail = views.NewsitemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^persons$', person_list, name='person-list'),
    url(r'^persons/(?P<pk>[0-9]+)$', person_detail, name='person-detail'),
    url(r'^courseresults/(?P<person_pk>[0-9]+)$', courseresult_list, name='courseresult-list'),
    url(r'^courseresults/(?P<person_pk>[0-9]+)/(?P<pk>[0-9]+)$', courseresult_detail, name='courseresult-detail'),
    url(r'^buildings$', building_list, name='building-list'),
    url(r'^buildings/(?P<pk>[0-9]+)$', building_detail, name='building-detail'),
    url(r'^testresults/(?P<person_pk>[0-9]+)$', testresult_list, name='testresult-list'),
    url(r'^testresults/(?P<person_pk>[0-9]+)/(?P<pk>[0-9]+)$', testresult_detail, name='testresult-detail'),
    url(r'^courses$', course_list, name='course-list'),
    url(r'^courses/(?P<pk>[0-9]+)$', course_detail, name='course-detail'),
    url(r'^schedules$', schedule_list, name='schedule-list'),
    url(r'^schedules/(?P<pk>[0-9]+)$', schedule_detail, name='schedule-detail'),
    url(r'^rooms$', room_list, name='room-list'),
    url(r'^rooms/(?P<pk>[0-9]+)$', room_detail, name='room-detail'),
    url(r'^groups$', group_list, name='group-list'),
    url(r'^groups/(?P<pk>[0-9]+)$', group_detail, name='group-detail'),
    url(r'^grouproles$', grouprole_list, name='grouprole-list'),
    url(r'^grouproles/(?P<pk>[0-9]+)$', grouprole_detail, name='grouprole-detail'),
    url(r'^newsfeeds$', newsfeed_list, name='newsfeed-list'),
    url(r'^newsfeeds/(?P<pk>[0-9]+)$', newsfeed_detail, name='newsfeed-detail'),
    url(r'^newsitems$', newsitem_list, name='newsitem-list'),
    url(r'^newsitems/(?P<pk>[0-9]+)$', newsitem_detail, name='newsitem-detail'),
]
