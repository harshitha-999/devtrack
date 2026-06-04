# Create your models here.
from django.db import models
from datetime import datetime



from abc import ABC, abstractmethod
from datetime import datetime


class BaseEntity(ABC):

    @abstractmethod
    def validate(self):
        pass

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
        }


class Reporter(BaseEntity):

    def __init__(self, id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team

    def validate(self):

        if not self.name:
            raise ValueError("Name cannot be empty")

        if '@' not in self.email:
            raise ValueError("Invalid email")

class Issue(BaseEntity):

    ALLOWED_STATUS = [
        "open",
        "in_progress",
        "resolved",
        "closed"
    ]

    ALLOWED_PRIORITY = [
        "low",
        "medium",
        "high",
        "critical"
    ]

    def __init__(
        self,
        id,
        title,
        description,
        status,
        priority,
        reporter_id
    ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = str(datetime.now())

    def validate(self):

        if not self.title:
            raise ValueError("Title cannot be empty")

        if self.status not in self.ALLOWED_STATUS:
            raise ValueError("Invalid status")

        if self.priority not in self.ALLOWED_PRIORITY:
            raise ValueError("Invalid priority")

    def describe(self):
        return f"{self.title} [{self.priority}]"
    
class CriticalIssue(Issue):

    def describe(self):
        return f"[URGENT] {self.title} — needs immediate attention"


class LowPriorityIssue(Issue):

    def describe(self):
        return f"{self.title} — low priority, handle when free"



'''
class Reporter(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Issue(models.Model):

    STATUS_CHOICES = [
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="medium"
    )

    
    reporter = models.ForeignKey(
        Reporter,
        on_delete=models.CASCADE,
        related_name="issues"
    )

    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


        
'''