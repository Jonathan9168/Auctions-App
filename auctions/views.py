import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.middleware import csrf
from django.shortcuts import get_object_or_404, render
from auctions.models import User, Item, Bid, Question, Answer
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from datetime import datetime
from django.conf import settings


def index(request):
    print(make_password("admin"))
    return HttpResponse("Hello, world. You're at the index.")


def spa_view(request):
    print(f"PATH is /: {request.path == '/'}")
    print(f"IS AUTHED: {request.user.is_authenticated}")
    if request.user.is_authenticated is False and (
            request.path != "/" and request.path != "/signup" and request.path != "/signup"):
        print("cant do this")
        return HttpResponse("You cannot access this page until you sign in")
    return render(request, 'auctions/spa/index.html', {})


def get_id(request):
    return JsonResponse({"id": request.user.id})


def logout_view(request):
    logout(request)
    response : any= HttpResponse()
    response.delete_cookie("logged")
    return response


def login_view(request):
    csrf_token = csrf.get_token(request)
    res : any  = HttpResponse("here have a csrf token :)")
    res.set_cookie('csrftoken', csrf_token)
    return res


def users_api(request: HttpRequest) -> JsonResponse or HttpResponse:
    """User API, allows for User data Retrieval via 'GET' request -> returns JSON response dict; User creation via 'POST' request;
     and User update via 'PUT' request"""
    if request.method == "GET":
        my_scheduled_job()
        return JsonResponse({'users': [user.to_dict() for user in User.objects.all()]})
    elif request.method == "POST":
        print(request.POST)
        if 'email' in request.POST:
            new_user = User(username=request.POST["email"], city=request.POST["city"],
                            dob=request.POST["dob"], email=request.POST["email"],
                            profile_picture=request.FILES["picture"])
            new_user.set_password(request.POST["password"])
            new_user.save()
            send_mail(
                        f"Welcome to quickAucs",
                        f'''
                        Thank you for signing up to quickAucs, we hope you enjoy buying and selling!

                        Kind regards,
                        QuickAucs Jonathan
                        ''',
                        settings.EMAIL_HOST_USER, 
                        [request.POST["email"]],
                        fail_silently=False,
                    )
            return JsonResponse({})
        else:
            print("LOGGER")
            print(json.loads(request.body))
            email : str = json.loads(request.body)["email"]
            password : str = json.loads(request.body)["password"]
            user = authenticate(username=email, password=password)
            response = HttpResponse("logged in")
            if user is not None:
                login(request, user)
                response.set_cookie('logged', "true")
                return response
            else:
                return HttpResponse("Your username and password didn't match. Please try again.")
    elif request.method == "PUT":
        request.method = "POST"
        print(request.FILES)
        user : int= User.objects.filter(id=request.POST["id"])
        user.update(
            city=request.POST["city"],
            dob=request.POST["dob"],
            email=request.POST["email"],
            username=request.POST["email"]
        )
        if "image" in request.FILES:
            user.update(profile_picture=request.FILES["image"])
        return JsonResponse({})


@login_required
def user_api(request, id):
    """Individual User API, allows for User data Retrieval via 'GET' request -> returns JSON response dict; 
    User deletion via 'DELETE' request;
    and User update via 'PUT' request"""
    if request.method == "GET":
        user : any= get_object_or_404(User, id=id)
        return JsonResponse({
            'user': [
                user.to_dict()
            ]
        })


@login_required
def items_api(request):
    """
    Items api to use to GET or POST objects in the database
    """
    my_scheduled_job()
    if request.method == "GET":
        return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })

    if request.method == "POST":
        if 'title' in request.POST:
            I = Item()
            I.user = request.user
            I.title : str = request.POST['title']
            I.description : str= request.POST['description']
            I.starting_price : int = request.POST['price']
            I.image : any = request.FILES["picture"]
            I.auction_end_time : any= request.POST['end_time']
            I.save()
        else:
            search = json.loads(request.body)["term"]
            return JsonResponse({
                'items': [
                    item.to_dict()
                    for item in Item.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
                ]
            })


@login_required
def item_api(request, id):
    """
    Individual item api used to delete, edit
    """
    my_scheduled_job()
    if request.method == "GET":
        item = get_object_or_404(Item, id=id)  # should send out a 404 if no id found
        return JsonResponse({
            'item': [
                item.to_dict()
            ]
        })

    if request.method == "DELETE":
        item = get_object_or_404(Item, id=id)
        item.delete()
        return JsonResponse({})


@login_required
def bids_api(request):
    """
    Bids api to use to GET or POST objects in the database
    """
    if request.method == "GET":
        return JsonResponse({
            'bids': [
                bid.to_dict()
                for bid in Bid.objects.all()
            ]
        })
    else:
        pass

    if request.method == "POST":
        B = Bid()
        i = get_object_or_404(Item, id=json.loads(request.body)['item'])
        B.user = get_object_or_404(User, id=json.loads(request.body)['user'])
        B.item = i
        B.price = json.loads(request.body)['bid']
        B.save()
        Item.objects.filter(id=i.id).update(
            starting_price=json.loads(request.body)['bid']
        )
        return JsonResponse({})


@login_required
def bid_api(request, id):
    """
    Individual bid api used to delete, edit
    """
    if request.method == "GET":
        bid : any= get_object_or_404(Bid, id=id)
        return JsonResponse({
            'bid': [
                bid.to_dict()
            ]
        })


@login_required
def questions_api(request):
    """
    Questions api to use to GET or POST objects in the database
    """
    if request.method == "GET":
        return JsonResponse({
            'questions': [
                question.to_dict()
                for question in Question.objects.all()
            ]
        })
    else:
        pass

    if request.method == "POST":
        variables = json.loads(request.body)
        Q = Question()
        Q.user : any = get_object_or_404(User, id=variables['user'])
        Q.item : any = get_object_or_404(Item, id=variables['item'])
        Q.question : any= variables['question']
        Q.save()
        return JsonResponse({})


@login_required
def question_api(request, id):
    """
    Individual question api used to delete, edit
    """
    if request.method == "GET":
        question : any= get_object_or_404(Question, id=id)
        return JsonResponse({
            'question': [
                question.to_dict()
            ]
        })


@login_required
def answers_api(request):
    """
    Answers api to use to GET or POST objects in the database
    """
    if request.method == "GET":
        return JsonResponse({
            'answers': [
                answer.to_dict()
                for answer in Answer.objects.all()
            ]
        })
    else:
        pass

    if request.method == "POST":
        variables = json.loads(request.body)
        A = Answer()
        A.user : any = get_object_or_404(User, id=variables['user'])
        A.question : any = get_object_or_404(Question, id=variables['question'])
        A.answer_text : str= variables['answer']
        A.save()
        return JsonResponse({})


@login_required
def answer_api(request, id):
    """
    Individual answer api used to delete, edit
    """
    if request.method == "GET":
        answer = get_object_or_404(Answer, id=id)
        return JsonResponse({
            'answer': [
                answer.to_dict()
            ]
        })

def my_scheduled_job():
    for item in Item.objects.all():
        if item.auction_end_time < datetime.now(): 
            all_bids : any= item.bid_set.all()
            price : int = 0
            if all_bids.count() == 0:
                send_mail(
                        f"Unfortunately your item '{item.title}' did not sell",
                        f'''
                        The item you posted on QuickAucs did not receive any bids.
                        Your item has been removed from the website and you need to relist it if you wish to sell it.

                        Kind regards,
                        QuickAucs Jonathan
                        ''',
                        settings.EMAIL_HOST_USER, 
                        [item.user.email],
                        fail_silently=False,
                    )
            else:
                big_bid : any= all_bids[all_bids.count()-1]
                price : int = big_bid.price
                send_mail(
                        f'Congratulations, you have won {item.title}',
                        f'''
                        You have won item {item.title} from QuickAucs.

                        The auction price is £{price}.
                        
                        Kind regards,
                        QuickAucs Atif
                        ''',
                        settings.EMAIL_HOST_USER,
                        [big_bid.user.email],
                        fail_silently=False,
                    )
            item.delete()