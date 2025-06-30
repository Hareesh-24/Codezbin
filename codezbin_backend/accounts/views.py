from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course, UserProfile
from django.views.decorators.csrf import csrf_exempt
import subprocess
import os
import tempfile
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
        else:
            print(form.errors)  # 👈 Debug: prints to console
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # or 'email'
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')  # redirect after login
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})



def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def personal_details_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/personal.html', {
        'user': request.user,
        'profile': profile
    })

@login_required
def privacy(request):
    return render(request, 'accounts/privacy.html')
@login_required
def terms_conditions(request):
    return render(request, 'accounts/termsandconditions.html')
@login_required
def certificates(request):
    return render(request, 'accounts/certificatenotyet.html')
@login_required
def help_center(request):
    return render(request, 'accounts/helpcenter.html')
@login_required
def settings(request):
    return render(request, 'accounts/settings.html')
@login_required
def course_dashboard(request):
    return render(request, 'accounts/coursedashboard.html')
@login_required
def career_guide(request):
    return render(request, 'accounts/careergui.html')
@login_required
def mentorship(request):
    return render(request, 'accounts/mentor.html')
@login_required
def video_tutorials(request):
    return render(request, 'accounts/vdotype.html')
@login_required
def books(request):
    return render(request, 'accounts/books.html')
@login_required
def text_editor(request):
    return render(request, 'accounts/textedi.html')

@login_required
def edit_personal_view(request):
    return render(request, 'accounts/edit_personal.html')


@login_required
def course_dashboard(request):
    courses = Course.objects.all()
    return render(request, 'accounts/course_dashboard.html', {'courses': courses})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Add the course to the user's enrolled courses
    profile.enrolled_courses.add(course)
    profile.save()
    
    # Optional: Redirect to course content or personal details
    return redirect('course_content', course_id=course.id)

@login_required
def course_content(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'accounts/course_content.html', {'course': course})

def python_course(request):
    return render(request, 'python_course.html')

@csrf_exempt
def run_code(request):
    output = ""
    code = ""
    language = ""
    
    if request.method == "POST":
        code = request.POST.get("code", "")
        language = request.POST.get("language", "").lower()  # Make it lowercase

        try:
            if language == "python":
                with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".py") as temp:
                    temp.write(code)
                    temp.flush()
                    output = subprocess.check_output(["python", temp.name], stderr=subprocess.STDOUT, text=True)
                os.remove(temp.name)

            elif language == "c":
                output = run_c_code(code)

            else:
                output = "Only Python and C are supported."

        except Exception as e:
            output = str(e)

    return render(request, 'accounts/textedi.html', {
        'output': output,
        'code': code,
        'language': language
    })



def run_c_code(code):
    try:
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            c_file_path = os.path.join(temp_dir, "program.c")
            exe_file_path = os.path.join(temp_dir, "program.exe")

            # Write the code to a temp C file
            with open(c_file_path, "w") as c_file:
                c_file.write(code)

            # Compile using gcc
            compile_result = subprocess.run(
                ["gcc", c_file_path, "-o", exe_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            # If there’s a compilation error
            if compile_result.returncode != 0:
                return compile_result.stderr

            # Run the executable
            run_result = subprocess.run(
                [exe_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=5,
            )

            return run_result.stdout or run_result.stderr

    except subprocess.TimeoutExpired:
        return "Error: Program took too long to run."
    except Exception as e:
        return f"Error: {str(e)}"
