from django.db import models

class MemberModel(models.Model):
    class Meta:
        db_table='member'
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    deathdate = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30)
    photo = models.FileField(default='static/default.jpg', upload_to='static/', blank=True)


def __str__(self):
    return "Name: {} {}".format(self.first_name, self.last_name)

class BandModel(models.Model):
    class Meta:
        db_table='band'
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(MemberModel, through='MembershipModel', null=True, blank=True)
    genre = models.CharField(max_length=50)
    history = models.CharField(max_length=255, null=True, blank=True)
    pic = models.FileField(default='static/default.jpg',upload_to='static/')


def __str__(self):
    return "Name: {}".format(self.name)


class MembershipModel(models.Model):
    class Meta:
        db_table='membership'
    id_member = models.ForeignKey(MemberModel, on_delete=models.CASCADE)
    id_band = models.ForeignKey(BandModel, on_delete=models.CASCADE)
    function = models.CharField(max_length=50)
    statuss = models.BooleanField(default=1)


def __str__(self):
    return "Band: {}, Member: {}".format(self.id_band, self.id_member)