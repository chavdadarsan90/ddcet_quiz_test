from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import DDCETQuestion, ExamResult

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz_home')
    else:
        form = UserCreationForm()
    return render(request, 'quiz/register.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz_home')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    # Notice we changed '-date_taken' to '-date' so it perfectly matches your database!
    results = ExamResult.objects.filter(user=request.user).order_by('-date')
    
    return render(request, 'quiz/dashboard.html', {'results': results})

@login_required(login_url='login')
def quiz_home(request):
    if request.method == 'POST':
        score = 0
        correct_answers = 0
        wrong_answers = 0
        review_data = []

        # અહીં ભૂલ હતી, જે મેં સુધારી દીધી છે (.getlist)
        question_ids = request.POST.getlist('question_ids')
        total_questions = len(question_ids)

        for q_id in question_ids:
            q = DDCETQuestion.objects.get(id=q_id)
            selected_option = request.POST.get(f'question_{q_id}', None)
            
            is_correct = False
            status = "Skipped ⚠️"

            if selected_option == q.correct_answer:
                score += 1
                correct_answers += 1
                is_correct = True
                status = "Correct ✅"
            elif selected_option is not None:
                score -= 0.25
                wrong_answers += 1
                status = "Wrong ❌"
            else:
                selected_option = "Not Attempted"

            review_data.append({
                'question': q,
                'selected_option': selected_option,
                'correct_answer': q.correct_answer,
                'status': status,
                'is_correct': is_correct
            })

        ExamResult.objects.create(
            user=request.user,
            score=score,
            total_questions=total_questions,
            correct_answers=correct_answers,
            wrong_answers=wrong_answers
        )
            
        return render(request, 'quiz/result.html', {
            'score': score, 
            'total': total_questions,
            'correct': correct_answers,
            'wrong': wrong_answers,
            'review_data': review_data
        })

    questions = DDCETQuestion.objects.order_by('?')[:25]
    return render(request, 'quiz/home.html', {'questions': questions})