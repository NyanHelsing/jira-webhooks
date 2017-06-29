from django.shortcuts import render
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from jira import JIRA


jira = JIRA(
    'https://openscience.atlassian.net',
    basic_auth=(os.environ['JIRA_USERNAME'], os.environ['JIRA_PASSWORD'])
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Hello': 'Goodbye'
    })


@api_view(['POST'])
def assign_to_josh(request, format=None):
    issue = jira.issue(request.data['issue']['id'])
    issue.update(assignee={'name': 'joshua.thomas.bird'})
    #new_issue = jira.create_issue(
    #    project='LABS',
    #    summary='New issue from jira-python',
    #    description='Look into this one',
    #    issuetype={'name': 'Bug'}
    #)
    return Response("SUCCESS");


# Create your views here.
