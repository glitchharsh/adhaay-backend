from django.db import models
from users.models import User
# Create your models here.
EVENTS = (
  ("OPEN_MIC","OPEN_MIC"),
  ("SUFI_NIGHT","SUFI_NIGHT"),
  ("BATTLE_OF_BANDS","BATTLE_OF_BANDS"),
  ("STUDENT_OF_THE_YEAR","STUDENT_OF_THE_YEAR"),
  ("VOICE_OF_HBTU","VOICE_OF_HBTU"),
  ("AWAKENINGS_DJ","AWAKENINGS_DJ"),
  ("BEAT_THE_STREET","BEAT_THE_STREET"),
  ("QUIZ_MARVEL","QUIZ_MARVEL"),
  ("SODA_POP","SODA_POP"),
  ("ROADIES","ROADIES"),
  ("MASQUERADE_PARTY","MASQUERADE_PARTY"),
  ("STUDENT_OF_THE_YEAR_2","STUDENT_OF_THE_YEAR_2"),
  ("CELEBRITY_NIGHT","CELEBRITY_NIGHT"),
  ("STUDENT_OF_THE_YEAR_3","STUDENT_OF_THE_YEAR_3"),
  ("TALENT_FIESTA","TALENT_FIESTA"),
  ("GUESS_THE_NAME","GUESS_THE_NAME"),
  ("AWAKENINGS_DJ_2","AWAKENINGS_DJ_2"),
  ("MURDER_MYSTERY","MURDER_MYSTERY"),
  ("BOLLYWOOD_PARTY","BOLLYWOOD_PARTY"),
  ("STUDENT_OF_THE_YEAR_4","STUDENT_OF_THE_YEAR_4"),
  ("OPEN_MIC_2","OPEN_MIC_2"),
  ("VOGUE","VOGUE"),
  ("STAGE_PERFORMANCES","STAGE_PERFORMANCES"),
  ("EDM_NIGHT","EDM_NIGHT"),
)

class Registration(models.Model):
  event = models.CharField(max_length=40, choices=EVENTS)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.user.name} [{self.user.email}] - {self.event}"

class EventRegistration(models.Model):
  event = models.CharField(max_length=40, choices=EVENTS)
  registrations = models.IntegerField()
  