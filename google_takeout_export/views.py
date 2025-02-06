from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def instructions(request):
    return render(request, 'instructions.html')

def privacy_notice(request):
    return render(request, 'privacy_notice.html')
    
def get_takeout_items(request, study_id="test"):
    # Define the takeout items for each study
    takeout_items = {
        'test': [
            "Location History (Timeline)",
            "Mail",
            "Messages",
            "My Activity"
        ],
    }

    # Get the takeout items for the given study_id
    items = takeout_items.get(study_id, [])

    # Return the items as a JSON response
    return JsonResponse({'items': items})


'''
Full list of possible takeout items as of February 2025:
[
    "Access Log Activity",
    "Alerts",
    "Android Device Configuration Service",
    "Arts & Culture",
    "Assignments",
    "Blogger",
    "Calendar",
    "Canvas",
    "Chrome",
    "Classroom",
    "Contacts",
    "Crisis User Reports",
    "Cursive",
    "Data Shared for Research",
    "Discover",
    "Drive",
    "Embark",
    "Firebase Dynamic Links",
    "Fit",
    "Fitbit",
    "Gemini",
    "Google Account",
    "Google Business Profile",
    "Google Chat",
    "Google Cloud Search",
    "Google Developers",
    "Google Earth",
    "Google Feedback",
    "Google Finance",
    "Google Help Communities",
    "Google Meet",
    "Google One",
    "Google Pay",
    "Google Photos",
    "Google Play Books",
    "Google Play Console",
    "Google Play Games Services",
    "Google Play Movies & TV",
    "Google Play Store",
    "Google Podcasts",
    "Google Shopping",
    "Google Store",
    "Google Translator Toolkit",
    "Google Workspace Marketplace",
    "Groups",
    "Home App",
    "Keep",
    "Location History (Timeline)",
    "Mail",
    "Maps",
    "Maps (your places)",
    "Messages",
    "My Activity",
    "My Maps",
    "Network Planner",
    "News",
    "Personal Safety",
    "Phone Audio",
    "Pinpoint",
    "Profile",
    "Purchases & Reservations",
    "Reminders",
    "Saved",
    "Search Contributions",
    "Search Notifications",
    "Street View",
    "Tasks",
    "Voice",
    "YouTube and YouTube Music",
]
'''
