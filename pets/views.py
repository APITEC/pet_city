from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pets.models import PetType, Pet, FoodType, Feeding
from pets.serializers import PetTypeSerializer, PetTypeDetailSerializer, PetSerializer, PetDetailSerializer, FoodTypeSerializer, FeedingSerializer, FeedingDetailSerializer


# Pet Type
class ListCreatePetType(ListCreateAPIView):
    queryset = PetType.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PetTypeDetailSerializer
        elif self.request.method == 'POST':
            return PetTypeSerializer


class RetrieveUpdateDestroyPetType(RetrieveUpdateDestroyAPIView):
    queryset = PetType.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PetTypeDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return PetTypeSerializer


# Pet
class ListCreatePet(ListCreateAPIView):
    queryset = Pet.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PetDetailSerializer
        elif self.request.method == 'POST':
            return PetSerializer


class RetrieveUpdateDestroyPet(RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PetDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return PetSerializer
            
        
# FoodType
class ListCreateFoodType(ListCreateAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class RetrieveUpdateDestroyFoodType(RetrieveUpdateDestroyAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    
    
# Feeding
class ListCreateFeeding(ListCreateAPIView):
    queryset = Feeding.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FeedingDetailSerializer
        elif self.request.method == 'POST':
            return FeedingSerializer


class RetrieveUpdateDestroyFeeding(RetrieveUpdateDestroyAPIView):
    queryset = Feeding.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FeedingDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return FeedingSerializer
