
from rest_framework import serializers
from .models import Repo


class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repo
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date',)
