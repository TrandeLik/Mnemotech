from django.db import models
import os


class TestModule(models.Model):
    quest = models.CharField(max_length=250, default="noQuest")
    otvet = models.CharField(max_length=250, default="noAnswer")
    rightotvet = models.CharField(max_length=250, default="noAnswer")
    ok = models.CharField(max_length=250, default="noAnswer")
    podsk = models.CharField(max_length=250,  default=".")
    podskScrita = models.CharField(max_length=250, default=" (Подсказка: )")

    def pod(self):
        self.podsk = self.podskScrita

    def okornot(self):
        if self.otvet == self.rightotvet:
            self.ok = "Right"
        else:
            self.ok = "Wrong"

    def __str__(self):
        return self.quest + "   -   " + self.ok + self.podsk


class conv(models.Model):
    before = models.CharField(max_length=250, default="abc")
    after = models.CharField(max_length=250, default="lol")

    def cnv(self):
        #result = os.popen("C:\cin.exe")
        output = subprocess.Popen([])

    def __str__(self):
        return self.before + " - " + self.after
