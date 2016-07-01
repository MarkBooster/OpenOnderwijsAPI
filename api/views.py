from collections import OrderedDict
from django.db.models import Q
from rest_framework import filters, viewsets, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.models import Person, Courseresult, Building, Testresult, \
    Course, Schedule, Room, Group, Grouprole, Newsfeed, Newsitem
from api.serializers import PersonSerializer, CourseresultSerializer, BuildingSerializer, \
    TestresultSerializer, CourseSerializer, ScheduleSerializer, RoomSerializer, \
    GroupSerializer, GrouproleSerializer, NewsfeedSerializer, NewsitemSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response(OrderedDict([
        ('persons', reverse('person-list', request=request, format=format)),
        ('buildings', reverse('building-list', request=request, format=format)),
        ('courses', reverse('course-list', request=request, format=format)),
        ('schedules', reverse('schedule-list', request=request, format=format)),
        ('rooms', reverse('room-list', request=request, format=format)),
        ('groups', reverse('group-list', request=request, format=format)),
        ('grouproles', reverse('grouprole-list', request=request, format=format)),
        ('newsfeeds', reverse('newsfeed-list', request=request, format=format)),
        ('newsitems', reverse('newsitem-list', request=request, format=format)),
    ]))

def get_view_name(view_cls, suffix=None):
    name = views.get_view_name(view_cls, suffix)
    if name == 'Api Root':
        return 'Open Onderwijs API'
    name += 's'
    return name

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = 'userId'

class CourseresultViewSet(viewsets.ModelViewSet):
    serializer_class = CourseresultSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = '-lastModified'

    def get_queryset(self):
        person_pk = self.kwargs['person_pk']
    	return Courseresult.objects.filter(student=person_pk)

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = 'buildingId'

class TestresultViewSet(viewsets.ModelViewSet):
    serializer_class = TestresultSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = '-lastModified'

    def get_queryset(self):
        person_pk = self.kwargs['person_pk']
    	return Testresult.objects.filter(userId=person_pk)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = '-lastModified'

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = '-lastModified'

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = 'roomId'

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = 'groupId'

class GrouproleViewSet(viewsets.ModelViewSet):
    queryset = Grouprole.objects.all()
    serializer_class = GrouproleSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = 'grouproleId'

class NewsfeedViewSet(viewsets.ModelViewSet):
    queryset = Newsfeed.objects.all()
    serializer_class = NewsfeedSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = '-lastModified'

class NewsitemViewSet(viewsets.ModelViewSet):
    queryset = Newsitem.objects.all()
    serializer_class = NewsitemSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = '-publishDate'
