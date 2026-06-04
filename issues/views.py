from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reporter

from .models import (
    Issue,
    CriticalIssue,
    LowPriorityIssue
)

@csrf_exempt
def issues(request):
    #breakpoint()

    if request.method == "POST":

        data = json.loads(request.body)

        try:

            if data["priority"] == "critical":

                issue = CriticalIssue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            elif data["priority"] == "low":

                issue = LowPriorityIssue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            else:

                issue = Issue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            issue.validate()

            with open("issues.json", "r") as f:
                issues = json.load(f)

            issues.append(
                issue.to_dict()
            )

            with open("issues.json", "w") as f:
                json.dump(issues, f)

            response = issue.to_dict()

            response["message"] = issue.describe()

            return JsonResponse(
                response,
                status=201
            )

        except ValueError as e:

            return JsonResponse(
                {"error": str(e)},
                status=400
            )
        
    elif request.method == "GET":

        with open("issues.json", "r") as f:
            issues = json.load(f)

        issue_id = request.GET.get("id")

        if issue_id:

            for issue in issues:

                if issue["id"] == int(issue_id):

                    return JsonResponse(
                        issue,
                        status=200
                    )

            return JsonResponse(
                {"error": "Issue not found"},
                status=404
            )
        status = request.GET.get("status")

        if status:

            filtered = []

            for issue in issues:

                if issue["status"] == status:
                    filtered.append(issue)

            return JsonResponse(
                filtered,
                safe=False
            )

        return JsonResponse(
            issues,
            safe=False
        )
    
@csrf_exempt
def reporters(request):

    if request.method == "POST":

        data = json.loads(request.body)

        try:

            reporter = Reporter(
                data["id"],
                data["name"],
                data["email"],
                data["team"]
            )

            reporter.validate()

            with open("reporters.json", "r") as f:
                reporters = json.load(f)

            reporters.append(
                reporter.to_dict()
            )

            with open("reporters.json", "w") as f:
                json.dump(reporters, f)

            return JsonResponse(
                reporter.to_dict(),
                status=201
            )

        except ValueError as e:

            return JsonResponse(
                {"error": str(e)},
                status=400
            )

    elif request.method == "GET":

        with open("reporters.json", "r") as f:
            reporters = json.load(f)

        reporter_id = request.GET.get("id")

        if reporter_id:

            for reporter in reporters:

                if reporter["id"] == int(reporter_id):
                    return JsonResponse(
                        reporter,
                        status=200
                    )

            return JsonResponse(
                {"error": "Reporter not found"},
                status=404
            )

        return JsonResponse(
            reporters,
            safe=False
        )