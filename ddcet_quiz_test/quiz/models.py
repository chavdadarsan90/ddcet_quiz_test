from django.db import models
from django.contrib.auth.models import User  # આ લાઈન ડેશબોર્ડ માટે ખૂબ જરૂરી છે
from django.db import models
from django.contrib.auth.models import User

# અપડેટ કરેલું પ્રશ્નો માટેનું ટેબલ (Bilingual - English & Gujarati)
class DDCETQuestion(models.Model):
    subject = models.CharField(max_length=100)
    
    # English Fields
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    
    # Gujarati Fields (blank=True, null=True એટલે રાખ્યું છે જેથી જૂના પ્રશ્નોમાં એરર ના આવે)
    question_text_guj = models.TextField(blank=True, null=True)
    option_a_guj = models.CharField(max_length=200, blank=True, null=True)
    option_b_guj = models.CharField(max_length=200, blank=True, null=True)
    option_c_guj = models.CharField(max_length=200, blank=True, null=True)
    option_d_guj = models.CharField(max_length=200, blank=True, null=True)

    correct_answer = models.CharField(max_length=1)

    def __str__(self):
        return f"[{self.subject}] {self.question_text}"

# તમારું જૂનું ExamResult ટેબલ એમનેમ જ રાખવું
class ExamResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    # --- NEW COLUMNS FOR DETAILED ANALYSIS ---
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    wrong_answers = models.IntegerField(default=0)
    skipped_questions = models.IntegerField(default=0)
    # -----------------------------------------

    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.user.username} - {self.score} Marks"