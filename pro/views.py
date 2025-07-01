import openai
import json
from pandas import read_csv
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect  # Add redirect to your imports
# Rename to distinguish from the function
from conn.models import savecontact as SaveContactModel
# Rename to distinguish from the function
from conn.models import submitreview as SubmitReviewModel
from django.http import JsonResponse


def aboutUs(request):
    return render(request, "about.html")


def home(request):
    if request.method == 'POST':
        search = request.POST.get('query', None)
        # Fetch details from CSV based on user input
        if search:
            result = find_details(search)
            if result:
                return render(request, 'index.html',{'result': result})
            else:            
                return render(request , 'index.html', {'error': 'No search result found.'})
    else:
        return render(request, "index.html")

def find_details(searched):
    data = read_csv("static/data.csv")
    
    for index, row in data.iterrows():
        if str(row['COMMON NAME']).lower() == str(searched).lower():
            return {
                'Common_Name': row['COMMON NAME'],
                'Botanical_Name': row['BOTANICAL NAME'],
                'Description': row['Description'],
                'Uses' : row['Uses'],
                'Locations': row['LOCATION'],
                'Img' : row['IMAGE']
                }
    return {}  # Return empty dictionary if spot not found



def zora(request):
    return render(request,"zora.html")


def contact(request):
    return render(request, "contact.html")


def thank_you_page(request):
    return render(request, "thankyou.html")


def savecontact(request):  # Changed function name to avoid conflict
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create and save contact
        en = SaveContactModel(name=name, email=email,
                              subject=subject, message=message)
        en.save()
        return redirect('thankyou')
    return render(request, "contact.html")


def submitreview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        year = request.POST.get('year')
        review = request.POST.get('review')
        en = SubmitReviewModel(name=name, course=course,
                               year=year, review=review)
        en.save()
        return redirect('thankyou')
    return render(request, "about.html")


# Replace with your OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"


@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            # Call OpenAI GPT API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ],
            )
            bot_reply = response["choices"][0]["message"]["content"]

            return JsonResponse({"reply": bot_reply})

        except Exception as e:
            return JsonResponse({"reply": "Sorry, I encountered an error!"}, status=500)