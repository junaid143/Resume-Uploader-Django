from django.shortcuts import render ,redirect
from django.views import View
from .forms import ResumeForm
from .models import Resume

# Create your views here.

class home(View):
    def get(self , request):
        print("Class Home method get ...")

        form = ResumeForm()
        
        return render(request , 'MyApp/home.html' , {'form':form})

    def post(self , request):
        print("Class Home method Post ...")
        form = ResumeForm(request.POST , request.FILES)
        if form.is_valid():
            print("Form Validated ...")
            form.save()
            print("Forms saved Successfully ..")
            return redirect('home')





class all_candidates(View):
    def get(self , request):
        print("Class all_candidates method get ...")
        data = Resume.objects.all()

        return render(request , 'MyApp/all_candidates.html' , {'data':data})

    def post(self , request):
        print("Class all_candidates method Post ...")
        data = Resume.objects.all()
        return render(request , 'MyApp/all_candidates.html' , {'data':data})





class candidate_info(View):
    def get(self , request , pk):
        print("Class candidate_info method get ...")

        data = Resume.objects.get(pk = pk)
        return render(request , 'MyApp/candidate_info.html' , {'d' : data})

    def post(self , request):
        print("Class candidate_info method Post ...")
        return render(request , 'MyApp/candidate_info.html')





class about(View):
    def get(self , request):
        print("Class about method get ...")
        return render(request , 'MyApp/about.html')

    def post(self , request):
        print("Class about method Post ...")
        return render(request , 'MyApp/about.html')






class contact(View):
    def get(self , request):
        print("Class Contact method get ...")
        return render(request , 'MyApp/contact.html')

    def post(self , request):
        print("Class contact method Post ...")
        return render(request , 'MyApp/contact.html')
