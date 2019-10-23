from rest_framework.serializers import ModelSerializer
from users.models import User
from pets.models import PetType, Pet, Feeding


class PetTypeSerializer(ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'


class FeedingSerializer(ModelSerializer):
    class Meta:
        model = Feeding
        fields = ['id', 'name', 'type', 'time']
        depth = 1


class PetSerializer(ModelSerializer):
    type = PetTypeSerializer()
    feedings = FeedingSerializer(source='feeding_set', many=True)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'type', 'birth_date', 'feedings']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(ModelSerializer):
    pets = PetSerializer(source='pet_set', many=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'birth_date', 'pets']