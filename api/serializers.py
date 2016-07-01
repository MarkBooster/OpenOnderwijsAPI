from api.models import Person, Courseresult, Building, Testresult, Course, Schedule, \
    Room, Group, Grouprole, Newsfeed, Newsitem
from rest_framework import serializers
from rest_framework.reverse import reverse

""" This mixin adds the primary key always to the result """
class WithPk(object):
    def get_pk_field(self, model_field):
        return self.get_field(model_field)

""" Persons """
class PersonSerializer(WithPk, serializers.ModelSerializer):
    # Cast to numeric values
    lat = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)
    lon = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)

    class Meta:
        model = Person
        fields = ('userId', 'givenname', 'surname', 'displayname', 'commonname',
            'nickname', 'affiliations', 'mail', 'telephonenumber', 'mobilenumber',
            'photoSocial', 'photoOfficial', 'gender', 'organization', 'department',
            'title', 'office', 'groups', 'lat', 'lon', 'lastModified')

""" Courseresults """
class CourseresultSerializer(WithPk, serializers.ModelSerializer):
    # student = serializers.HyperlinkedRelatedField(read_only=True, view_name='person-detail')

    class Meta:
        model = Courseresult
        fields = ('courseresultId', 'student', 'course', 'testresults', 'lastModified', 'grade', 'comment', 'passed')

""" Buildings """
class BuildingSerializer(WithPk, serializers.ModelSerializer):
    # Cast to numeric values
    lat = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)
    lon = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)

    class Meta:
        model = Building
        fields = ('buildingId', 'abbreviation', 'name', 'description', 'address',
            'postalCode', 'city', 'lat', 'lon', 'altitude', 'lastModified')


class CourseresultHyperlink(serializers.HyperlinkedRelatedField):
    def use_pk_only_optimization(self):
        return False

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'person_pk': obj.student.userId,
            'pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

""" Testresults """
class TestresultSerializer(WithPk, serializers.ModelSerializer):
    courseresult = CourseresultHyperlink(read_only=True, view_name='courseresult-detail')

    class Meta:
        model = Testresult
        fields = ('testresultId', 'courseId', 'courseresult', 'userId', 'description',
            'lastModified', 'assessmentType', 'testDate', 'grade', 'comment',
            'passed', 'weight')

""" Courses """
class CourseSerializer(WithPk, serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('courseId', 'name', 'abbr', 'ects', 'description', 'goals',
            'requirements', 'level', 'format', 'language', 'enrollment', 'literature',
            'exams', 'schedule', 'link', 'organization', 'department', 'lecturers',
            'groups', 'lastModified')

""" Schedules """
class ScheduleSerializer(WithPk, serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('scheduleId', 'userId', 'roomId', 'buildingId', 'courseId',
            'startDateTime', 'endDateTime', 'groupId', 'lecturers', 'description',
            'lastModified')

""" Rooms """
class RoomSerializer(WithPk, serializers.ModelSerializer):
    # Cast to numeric values
    lat = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)
    lon = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)

    class Meta:
        model = Room
        fields = ('roomId', 'buildingId', 'abbreviation', 'name', 'description',
            'totalSeats', 'totalWorkspaces', 'availableWorkspaces', 'lat', 'lon',
            'altitude', 'lastModified')

""" Groups """
class GroupSerializer(WithPk, serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('groupId', 'name', 'description', 'type', 'members', 'courses', 'lastModified')

""" Grouproles """
class GrouproleSerializer(WithPk, serializers.ModelSerializer):
    class Meta:
        model = Grouprole
        fields = ('grouproleId', 'group', 'person', 'role', 'lastModified')

""" Newsfeeds """
class NewsfeedSerializer(WithPk, serializers.ModelSerializer):
    class Meta:
        model = Newsfeed
        fields = ('newsfeedId', 'title', 'description', 'items', 'groups', 'lastModified')

""" Newsitems """
class NewsitemSerializer(WithPk, serializers.ModelSerializer):
    class Meta:
        model = Newsitem
        fields = ('newsitemId', 'feeds', 'publishDate', 'title', 'authors', 'image', 'link', 'content')
