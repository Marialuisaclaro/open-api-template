import factory


class NameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'example.Name'

    name = factory.Faker('first_name')
