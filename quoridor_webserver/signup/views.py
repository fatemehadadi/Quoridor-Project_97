from django.shortcuts import render
import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from signup.models import Users

# Create your views here.

def is_username_valid_signin(username):
    if username:
        return True
    return False


def is_password_valid_signin(password):
    if password:
        return True
    return False


def index_signin(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Error: Send your data via POST.")

    post = request.POST.dict()

    # whether data is valid.

    if (set(post.keys()) != {"action", "username", "password"}
        or not is_username_valid_signin(post["username"].lower())
        or not is_password_valid_signin(post["password"])
        ):
        return HttpResponseBadRequest("Error: Your POST data is corrupted.")

    # checking user from database.

    try:
        user = Users.objects.get(username=post["username"].lower())
    except Users.DoesNotExist:
        return HttpResponseForbidden("No such user exists.")

    # Verify password_hash and intered password.

    if post["password"] != user.password_hash:
        return HttpResponseForbidden("Your password is incorrect.")

    # Setting username for session.

    request.session['username'] = user.username
    return HttpResponse(
        "Welcome %s! Your entered time is: %s"
        % (user.name,
           str(datetime.datetime.now())

           ))


# Check whether username is valid or not.


def is_username_valid(username):
    if (3 <= len(username) <= 100
        and username.replace('_', '').isalnum()
        and (username[0].isalpha() or username[0] == '_')
        ):
        return True
    return False

# Check whether password is valid or not.


def is_password_valid(password):
    if len(password) >= 8:
        return True
    return False


# Check whether name is valid or not.


def is_name_valid(name):
    if 0 <= len(name) <= 100:
        return True
    return False


# Signing up on the site.


def index(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Send your data via POST!")

    post = request.POST.dict()
    print(post)
    print(post["action"])

    if post["action"] == "signin":
        index_signin(request)
        return HttpResponse("Good to see you!")
        # whether data is valid.

    if not is_name_valid(post["name"]) or not is_username_valid(post["username"].lower()) or not is_password_valid(
            post["password"]):
        return HttpResponseBadRequest("Your POST data is corrupted!")

    # if username exists.

    if Users.objects.filter(username=post["username"].lower()):
        return HttpResponseBadRequest("This username already exists.")

    # Creating user.

    Users.objects.create(name=post["name"],

                         username=post["username"].lower(),

                         password_hash=post["password"],

                         )

    return HttpResponse("Registration has been completed.")
