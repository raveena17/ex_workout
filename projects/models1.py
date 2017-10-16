"""
    Project Models
"""
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from project_management.milestone.models import Milestone
from project_management.business_unit.models import BusinessUnit
from project_management.users.models import UserProfile


class ProjectType(models.Model):
    """
        Represent the Project Type
    """
    name = models.CharField(max_length = 120)
    level = models.IntegerField(null = True,  blank = True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class DevelopmentProcess(models.Model):
    """
        Represents the development process of the project
    """
    name = models.CharField(max_length = 120)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Domain(models.Model):
    """
        Represents the Domain of the project
    """
    name = models.CharField(max_length = 120)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Technology(models.Model):
    """
        Represents the Technology used in project
    """
    name = models.CharField(max_length = 120)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Technology')
        verbose_name_plural = _('Technologies')
        ordering = ['name']

class DevelopmentEntity(models.Model):
    """
        Represents the Development Entities need for the project
    """
    HARDWARE = 'hardware'
    SOFTWARE = 'software'
    RESOURCE_CATEGORY = ((HARDWARE, 'hardware'), (SOFTWARE, 'software'))
    name = models.CharField(_('resource'), max_length = 120,)
    quantity = models.IntegerField(_('quantity'), default = 1)
    category = models.CharField(_('category'), max_length = 8, blank = True,
                choices=RESOURCE_CATEGORY)

    def __unicode__(self):
        return '%s - (%d)nos' % (self.name, self.quantity)

    class Meta:
        verbose_name = _('DevelopmentEntity')
        verbose_name_plural = _('DevelopmentEntities')

class ProjectSchedule(models.Model):
    """
        Represents the schedule of the project
    """
    expected_start_date = models.DateField(_('Expected Start Date'),
        null=True, blank = True)
    expected_end_date = models.DateField(_('Expected End Date'),
        null = True, blank = True)
    planned_start_date = models.DateField(_('Planned Start Date'),
        null = True, blank = True)
    planned_end_date = models.DateField(_('Planned End Date'),
        null = True, blank = True)
    approval_date = models.DateField(_('Approval Date'),
        null = True, blank = True)
    kick_off_meeting_planned_date = models.DateField(
        _('Kick Off Meeting Planned Date'), null = True, blank = True)
    kick_off_meeting_actual_date = models.DateField(
        _('Kick Off Meeting Actual Date'), null = True, blank = True)
    actual_start_date = models.DateField(_('Actual Start Date'),
        null = True, blank = True)
    actual_end_date = models.DateField(_('Actual End Date'),
        null = True, blank = True)
    initiation_request_date = models.DateField(_('Requested By'),
        null = True, blank = True)
    approved_date = models.DateField(_('Approved on'),
        null = True, blank = True)
    next_invoice_date = models.DateField(_('Next Invoice Date'),
        null = True, blank = True)
    

    def __unicode__(self):
        return '(%s,%s)' % (self.planned_start_date, self.planned_end_date)

    class Meta:
        verbose_name = _('Project Schedule')
        verbose_name_plural = _('Project Schedule')

class ProjectDetail(models.Model):
    """
        Represent the project details
    """
    version_no = models.CharField(_('Version Number'),
        max_length = 20, null=True, blank=True)
    approval_reference = models.CharField(_('Approval Reference Detail'),
        max_length = 300, null = True, blank = True)
    project_type = models.ForeignKey(ProjectType,
        verbose_name = _('Project Type'))
    objective = models.TextField(_('Project Objectives'), null=True, blank=True)
    goals = models.TextField(_('5G Goals'), null=True, blank=True)
    project_scope = models.TextField(_('Scope of Project'),
        null = True, blank = True)
    development_process = models.ForeignKey(DevelopmentProcess,
        verbose_name = _('Development Process'), null=True, blank=True,
        related_name = '%s(class)s_development_process')
    technology = models.ManyToManyField(Technology, null=True, blank=True,
        verbose_name = _('technology'), related_name = '%s(class)s_technology')
    development_environment = models.ManyToManyField(DevelopmentEntity,
        null=True, blank=True, verbose_name=_('Development Environment'),
        related_name = '%s(class)s_development_environment')

    class Meta:
        abstract = True

class Project(ProjectDetail):
    """
        Represents the Project
    """
    INTERNAL = 'internal'; EXTERNAL = 'external'
   
    approval_choices = ((INTERNAL, 'internal'), (EXTERNAL, 'external'))
   
    code = models.CharField(unique=True, max_length = 100)
    name = models.CharField(_('Project Name'), max_length = 120, unique=True)
    project_no = models.IntegerField(_('Project Id'))
    short_name = models.CharField(_('Short Name'), max_length = 80)
    business_unit = models.ForeignKey(BusinessUnit, null = True, blank = True,
                                related_name = '%s(class)s_business_unit',
                                verbose_name = _('Division'))
    parent = models.ForeignKey('self', null = True, blank = True,
            related_name = '%s(class)s_parent', verbose_name = _('Parent'))
    apex_body_owner = models.ForeignKey(User, null=True, blank = True,
        verbose_name = _('Apex Body Owner'), related_name = '%s(class)s_apex')
    owner = models.ForeignKey(User, verbose_name =
        _('Project Manager/Lead'), related_name = '%s(class)s_owner',
        null=True, blank=True)
    approval_type = models.CharField(_('Approval Type'),
                        max_length = 120, choices = approval_choices)
    
    planned_effort = models.DecimalField(_('Estimated Effort(man-days)'), null=True,
        blank=True, help_text=_('In Days'), max_digits=10, decimal_places=2)
    schedules = models.ForeignKey(ProjectSchedule, null=True,
        blank=True, verbose_name = _('Project Schedule'))
    domain = models.ForeignKey(Domain, verbose_name = _('Domain'),
        null=True, blank=True)
    customer = models.ForeignKey(BusinessUnit, verbose_name = _('Client Details'),
       related_name='%s(class)s_customer', null=True, blank=True)
    customer_contact = models.ForeignKey(UserProfile,
        verbose_name = _('Client Details'), null=True, blank=True)
    milestone = models.ManyToManyField(Milestone,
        verbose_name =  _('Milestone'))
    team = models.ManyToManyField(User, through = 'ProjectMembership',
                                  related_name = '%s(class)s_team',
                                  verbose_name = _('team'), null = True)
    requested_by = models.ForeignKey(User, verbose_name = _('Requested By'),
        related_name = '%s(class)s_requested_by', null = True)
    approved_by = models.ForeignKey(User, verbose_name = _('Request To'),
        related_name = '%s(class)s_approved_by', null = True )
    other_project_type = models.CharField(_('Other_project_type'),
        max_length = 128, null = True, blank = True)
    is_project_group = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_approved = models.BooleanField(default = True)
    cancel = models.BooleanField(default = False)
    project_owner = models.ForeignKey(User, null=True, blank = True,
        verbose_name = _('project_owner'), related_name = '%s(class)s_project_owner')
    estimated_time_exceed = models.BooleanField()
    rejection_reason = models.TextField()
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'projects.views.project_initiation'

    def save(self, **kwargs):
        if not self.id:
            self.project_no = Project.objects.aggregate(
                        models.Max('project_no'))['project_no__max']+1
            auto_id = self.project_no
            year = datetime.now().year
            customer_name = str(self.customer) if self.customer else self.INTERNAL
            self.code = '-'.join(map(slugify, [auto_id, customer_name,
                                             self.short_name, year]))
        super(Project, self).save(**kwargs)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

class ProjectMembership(models.Model):
    """
        Represents the Project Team
    """
    project = models.ForeignKey(Project)
    member = models.ForeignKey(User)
    roles = models.ManyToManyField(Group)

    def __unicode__(self):
        return '%s - %s' % (self.project.name, self.member.username)

class ProjectRole(models.Model):
    """
        Group that plays a role in any project.
    """
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return '%s' % self.group.name
