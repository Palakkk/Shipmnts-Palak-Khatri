from django.shortcuts import render,redirect
from app.models import *

# Create your views here.
def register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        password1=request.POST['password']
        print(name1,email1,password1)
        data=UserRegister(name=name1,email=email1,password=password1)
        a=UserRegister.objects.filter(email=email1)
        if len(a)==0:
            data.save()
            return redirect('login1')
        else:
            return render(request,'register.html',{'message':"user alredy exist"}) 
    return render(request,'register.html')  

def login(request):
    if request.method == "POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            data=UserRegister.objects.get(email=email1,password=password1)
            if data:
                request.session['email']=data.email
                print(request.session['email'])
                return redirect('index')
            else:
                return render(request,'login.html',{'message':'Invalid email or password'})
        except:
            return render(request,'login.html',{'message':'Invalid email or password'})
    return render(request,'login.html')

def index(request):
    if 'email' in request.session:
        e=request.session['email']
        all_data=UserRegister.objects.all()
        data=UserRegister.objects.get(email=e)


        # common questions section
        if(Question.objects.exists()):
            all_ques=Question.objects.order_by('-created_at', '-updated_at')
        else:
            all_ques=None

        new_ques=None
        # create new ques
        if request.method=="POST":
            question=request.POST.get('question')
            new_ques=Question(user=data, question=question)
            new_ques.save()
        else:
            pass
        context={
                        'all_data':all_data,
                        'data':data,
                        'all_ques':all_ques,
                        'new_ques':new_ques,
                        # 'comments':comments,
                    }
        return render(request,'index.html',context)

    else: 
        return render(request,'login.html')

    # def add_comment(request):
    #     if request.method == 'POST':
    #         user_data = UserRegister.objects.get(email=request.session['email'])
    #         text = request.POST.get('text')
    #         user = user_data
    #         ques_id = request.POST.get('ques_id')
    #         # h=UserPost.objects.
    #         post_user=Question.objects.get(id=ques_id)
    #         new_comment = Comments.objects.create(user=user, comment=text, question=post_user.question)
    #         new_comment.save()

    #         comments = Comments.objects.filter(question=post_user.question)
 
    #         
    
def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return redirect('login1')


