from .models import Jadwal
from rest_framework import serializers

class JadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadwal
        fields = ['id','tanggal','imsak','subuh','duha','zuhur','asar','magrib','isya']