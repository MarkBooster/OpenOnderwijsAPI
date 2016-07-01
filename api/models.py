from __future__ import unicode_literals

from django.db import models

def selfzip(a):
    return zip(a, a)

class Affiliation(models.Model):
    affiliationId = models.CharField(primary_key=True, max_length=255)
    affiliation = models.CharField(max_length=32, help_text='as defined in eduPerson')

    def __str__(self):
        return self.affiliation

class Person(models.Model):
    GENDERS = ('M', 'F', 'U', 'X')

    userId          = models.CharField(primary_key=True, max_length=255)
    givenname       = models.CharField(max_length=255)
    surname         = models.CharField(max_length=255)
    displayname     = models.CharField(max_length=255)
    commonname      = models.CharField(null=True, max_length=255)
    nickname        = models.CharField(null=True, max_length=255)
    affiliations    = models.ManyToManyField('Affiliation', blank=True)
    mail            = models.EmailField(null=True)
    telephonenumber = models.CharField(null=True, max_length=32)
    mobilenumber    = models.CharField(null=True, max_length=32)
    photoSocial     = models.URLField(null=True)
    photoOfficial   = models.URLField(null=True)
    gender          = models.CharField(null=True, choices=selfzip(GENDERS), max_length=1)
    organization    = models.CharField(max_length=255)
    department      = models.CharField(null=True, max_length=255)
    title           = models.CharField(null=True, max_length=255)
    office          = models.CharField(null=True, max_length=255)
    groups          = models.ManyToManyField('Group', through='Grouprole', blank=True)
    lat             = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    lon             = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    lastModified    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.displayname

class Courseresult(models.Model):
    courseresultId = models.CharField(primary_key=True, max_length=255)
    student        = models.ForeignKey('Person')
    course         = models.ForeignKey('Course')
    # course.lastModified?
    lastModified   = models.DateTimeField(auto_now=True)
    grade          = models.CharField(null=True, max_length=15)
    comment        = models.TextField(null=True)
    passed         = models.NullBooleanField()

class Building(models.Model):
    buildingId   = models.CharField(primary_key=True, max_length=255)
    abbreviation = models.CharField(max_length=32)
    name         = models.CharField(max_length=255)
    description  = models.TextField()
    address      = models.CharField(null=True, max_length=256)
    postalCode   = models.CharField(null=True, max_length=16)
    city         = models.CharField(max_length=255)
    lat          = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    lon          = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    altitude     = models.DecimalField(null=True, max_digits=3, decimal_places=2)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.abbreviation

class Testresult(models.Model):
    testresultId   = models.CharField(primary_key=True, max_length=255)
    # testresult.lastModified?
    courseId       = models.ManyToManyField('Course', related_name='+', blank=True)
    courseresult   = models.ForeignKey('Courseresult', related_name='testresults')
    userId         = models.ManyToManyField('Person', related_name='+', blank=True)
    description    = models.CharField(max_length=255)
    lastModified   = models.DateTimeField(auto_now=True)
    assessmentType = models.CharField(null=True, max_length=255)
    testDate       = models.DateField()
    grade          = models.CharField(max_length=255)
    comment        = models.TextField()
    passed         = models.NullBooleanField()
    weight         = models.PositiveSmallIntegerField(null=True)

class Course(models.Model):
    LEVELS    = ('HBO-B', 'HBO-M', 'WO-B', 'WO-M', 'WO-D')
    LANGUAGES = ('nl-NL', 'en-US', 'de-DE')

    courseId     = models.CharField(primary_key=True, max_length=255)
    name         = models.CharField(max_length=255)
    abbr         = models.CharField(null=True, max_length=32)
    ects         = models.PositiveIntegerField(null=True)
    description  = models.TextField()
    goals        = models.TextField(null=True)
    requirements = models.TextField(null=True)
    level        = models.CharField(null=True, choices=selfzip(LEVELS), max_length=8)
    format       = models.TextField(null=True)
    language     = models.CharField(choices=selfzip(LANGUAGES), max_length=2)
    enrollment   = models.TextField(null=True)
    literature   = models.TextField(null=True)
    exams        = models.TextField(null=True)
    schedule     = models.TextField(null=True)
    link         = models.URLField(null=True)
    organization = models.CharField(null=True, max_length=255)
    department   = models.CharField(null=True, max_length=255)
    lecturers    = models.ManyToManyField('Person', related_name='+', blank=True)
    groups       = models.ManyToManyField('Group', related_name='courses', blank=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    scheduleId    = models.CharField(primary_key=True, max_length=255)
    userId        = models.ManyToManyField('Person', related_name='+', blank=True)
    roomId        = models.ManyToManyField('Room', related_name='+', blank=True)
    buildingId    = models.ManyToManyField('Building', related_name='+', blank=True)
    courseId      = models.ManyToManyField('Course', related_name='+', blank=True)
    startDateTime = models.DateTimeField(null=True)
    endDateTime   = models.DateTimeField(null=True)
    groupId       = models.ManyToManyField('Group', related_name='+', blank=True)
    lecturers     = models.ManyToManyField('Person', related_name='+', blank=True)
    description   = models.TextField(null=True)
    lastModified  = models.DateTimeField(auto_now=True)

class Room(models.Model):
    roomId              = models.CharField(primary_key=True, max_length=255)
    buildingId          = models.ForeignKey('Building', related_name='rooms')
    abbreviation        = models.CharField(max_length=32)
    name                = models.CharField(max_length=255)
    description         = models.TextField(null=True)
    totalSeats          = models.PositiveIntegerField(null=True)
    totalWorkspaces     = models.PositiveIntegerField(null=True)
    availableWorkspaces = models.PositiveIntegerField(null=True)
    lat                 = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    lon                 = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    altitude            = models.DecimalField(null=True, max_digits=3, decimal_places=2)
    lastModified        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.abbreviation

class Group(models.Model):
    GROUP_TYPES = ('?LesGroep','?LeerGroep','ou','affiliation','Generic')

    groupId      = models.CharField(primary_key=True, max_length=255)
    name         = models.CharField(max_length=255)
    description  = models.TextField(null=True)
    type         = models.CharField(choices=selfzip(GROUP_TYPES), max_length=32)
    members      = models.ManyToManyField('Person', through='Grouprole', blank=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Grouprole(models.Model):
    ROLES = ('member', 'manager', 'administrator')

    grouproleId  = models.CharField(primary_key=True, max_length=255)
    group        = models.ForeignKey('Group')
    person       = models.ForeignKey('Person')
    role         = models.CharField(choices=selfzip(ROLES), max_length=32)
    lastModified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('person', 'group')

class Newsfeed(models.Model):
    newsfeedId    = models.CharField(primary_key=True, max_length=255)
    title         = models.CharField(max_length=255)
    description   = models.TextField(null=True)
    groups        = models.ManyToManyField('Group', related_name='+', blank=True)
    lastModified  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Newsitem(models.Model):
    newsitemId    = models.CharField(primary_key=True, max_length=255)
    feeds         = models.ManyToManyField('Newsfeed', related_name='items', blank=True)
    publishDate   = models.DateTimeField()
    title         = models.CharField(max_length=255)
    authors       = models.CharField(max_length=255, null=True)
    image         = models.URLField(null=True)
    link          = models.URLField(null=True)
    content       = models.TextField()

    def __str__(self):
        return self.title
