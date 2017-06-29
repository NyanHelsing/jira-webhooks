from django.shortcuts import render

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

    return Response('HELLO');


# Create your views here.
