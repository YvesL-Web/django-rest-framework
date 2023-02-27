from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Rest framework import
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

# from .forms import UserRegisterForm
from contacts.models import Contact
from .serializers import UserCreateSerializer, UserSerializer

# from .models import User

# Create your views here.
# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST or None)
#         if form.is_valid():
#             # Check Username
#             if User.objects.filter(username=form.cleaned_data.get('username')).exists():
#                 messages.error(request,'That Username is taken!')
#                 return redirect('user:register')
#             elif User.objects.filter(email=form.cleaned_data.get('email')).exists():
#                 messages.error(request, 'That email is being used!')
#                 return redirect('user:register')
#         new_user = form.save()
#         username = form.cleaned_data.get('username')
#         messages.success(request, f"Hey {username}, Your account was created successfully")
#         return redirect('users:login')
#     else:
#         form = UserRegisterForm()
        

#     context = {
#         'form': form,
#     }
#     return render(request,'users/register.html',context)

# def login_view(request):

#     if request.user.is_authenticated:
#         return redirect("pages:index")
    
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
        
#         try:
#             user = User.objects.get(email=email)
#             user = authenticate(request, email=email, password=password)      
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "You are logged in!")
#                 return redirect("pages:index")
#             else:
#                 messages.warning(request, "email or password is incorrect")
#                 return redirect("users:login")
#         except:
#             messages.warning(request, f'User does not exist !.')
        
#     return render(request, "users/login.html")

# def logout_view(request):
#     logout(request)
#     messages.success(request, "You are now logged out!")
#     return redirect('pages:index')

# def dashboard(request):
#     user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
#     context = {
#         'contacts' : user_contacts
#     }
#     return render(request, 'users/dashboard.html',context)

# classBased View
class RegisterView(APIView):   
    def post(self, request):
        data = request.data

        serializer = UserCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_201_CREATED)

class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        user= UserSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)