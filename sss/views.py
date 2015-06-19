
from sss.models import UserProfile
from django.template import RequestContext
from django.shortcuts import render
from models import *
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


#from sss.serializer import BeerSerializer
from sss.forms import *
from django.views.generic.edit import FormView
# Create your views here.
def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')
def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__startswith=starts_with)
    else:
        cat_list = Category.objects.all()

    if max_results > 0:
        if (len(cat_list) > max_results):
            cat_list = cat_list[:max_results]

    for cat in cat_list:
        cat.url = encode_url(cat.name)
    
    return cat_list
def home(request):
	return render(request, 'home.html')


def add(request):
	if request.method == 'POST':
		author = Author.objects.create(first_name=request.POST.get('firstname'), last_name=request.POST.get('lastname'), email=request.POST.get('email'),phonenumber =request.POST.get('phonenumber'),address=request.POST.get('adddress'),state=request.POST.get('sttate'),city=request.POST.get('ciity'),country=request.POST.get('couuntry'))
		author.save()
		
                return render(request, 'new2.html')
	else:
		return render(request, 'home.html')

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
	if request.method == 'POST':
		publisher = Publisher.objects.create(name=request.POST.get('name'), address=request.POST.get('address'), city=request.POST.get('city'), state_province=request.POST.get('state'), website=request.POST.get('web'))
		publisher.save()
		name=publisher.name
		address=publisher.address
		return render(request, 'home.html')
	else:
		return render(request, 'new2.html')
def index2(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
	if request.method == 'POST':
		publisher = Page.objects.create(title=request.POST.get('title'), url=request.POST.get('url'), views=request.POST.get('views'))
		publisher.save()
		return render(request, 'home.html')
	else:
		return render(request, 'new.html')
	
	
  
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.


#def contact(request):
#	if request.method == 'POST':
#		form = ContactForm(request.POST)
#		if form.is_valid():


	
#			return HttpResponseRedirect('new3.html')
#	else:
#		form = ContactForm()
#	return render(request, 'home.html', {'form' : form})



#def firstfrom(request):

#	form = PostForm(request.POST)
#	if form.is_valid():
#		post=form.save()
#		post.save()
#		return redirect('home')


#def secondform(request):
#	form = CommmentForm(request.POST)
#	if form.is_valid():
#		comment = form.save()

#		comment.save()
#def contact(request):
 #   if request.method == 'POST': # If the form has been submitted...
     #   form = ContactForm(request.POST) # A form bound to the POST data
  #      if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
   #         return HttpResponseRedirect('/thanks/') # Redirect after POST
    #else:
     #   form = ContactForm() # An unbound form

    
#return render(request, 'contact.html', {
 #       'form': form,
    #})
#def login(request):
#	if request.method == 'POST':
#		author = Author.objects.get('firstname')
 #               author2 = Author.objects.get('lastname') 
#		if (firstname == author && lastname == author2):
#		
 #               return render(request, 'new2.html')
#	else:
#		return render(request, 'home.html')

# List our beers and add beers
#class BeerList(generics.ListCreateAPIView):
 #   queryset = Beer.objects.all()
  #  serializer_class = BeerSerializer
 
 
# Get a beer and remove a beer
#class BeerDetail(generics.RetrieveDestroyAPIView):
 #   queryset = Beer.objects.all()
  #  serializer_class = BeerSerializer

def register(request):

    
    registered = False

   
    if request.method == 'POST':
       
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('profile.html')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/home/')
def family(request):

    
    familyentered= False

   
    if request.method == 'POST':
       
        family_form = FamilyForm(data=request.POST)
        

        # If the two forms are valid...
        if family_form.is_valid():
            # Save the user's form data to the database.
            family = family_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            
            family.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            

            # Now we save the UserProfile model instance.
           
            # Update our variable to tell the template registration was successful.
            familyentered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        family_form = FamilyForm()
       

    # Render the template depending on the context.
    return render(request,
            'family.html',
            {'family_form': family_form,  'familyentered': familyentered} )



def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('family')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
@login_required
def profile(request):
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {'cat_list': cat_list}
    u = User.objects.get(username=request.user)
    
    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None
    
    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render(request,'login/profile.html', context_dict)
