from django.conf import settings
from konstantin.utils import ChoiceEnum


class ProjectState(ChoiceEnum):
    CONCEPT = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    STOPPED = 4

    _choices = (
        (CONCEPT, "Concept"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
        (STOPPED, "Stopped"),
    )


class ProjectType(ChoiceEnum):
    WEBSITE = 0
    APPLICATION = 1
    ELECTRONICS = 2
    MUSIC = 4

    _choices = (
        (WEBSITE, "Website"),
        (APPLICATION, "Application"),
        (ELECTRONICS, "Electronics"),
        (MUSIC, "Music"),
    )

class ProjectRole(ChoiceEnum):
    PRODUCER = 0
    COMPOSER = 1
    DESIGNER = 2
    PROGRAMMER = 4
    CODE_MAINTENANCE = 8

    _choices = (
        (PRODUCER,'Producer'),
        (COMPOSER,'Composer'),
        (DESIGNER,'Designer'),
        (PROGRAMMER,'Programmer'),
        (CODE_MAINTENANCE, 'Code Maintenance'),
    )
