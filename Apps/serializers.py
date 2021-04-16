from rest_framework import serializers
from .models import Todos


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ('id', 'title', 'description', 'completed')


# from rest_framework import serializers
# from .models import Todos


# class TodosSerializer(serializers.ModelSerializer):
#       class Sub:
#            model=Todos
#            fields=['id','title','description','completed']
           
      