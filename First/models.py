from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=125)
    plan = models.FloatField()
    description = models.CharField(max_length=500)


class BillsCategory(models.Model):
    name = models.CharField(max_length=125, unique=True)


class Bill(models.Model):
    name = models.CharField(max_length=125)
    summ = models.FloatField()
    description = models.CharField(max_length=500)
    bills_category = models.ForeignKey(BillsCategory, on_delete=models.CASCADE)


class Currency(models.Model):
    name = models.CharField(max_length=125, null=False)


class Incomes(models.Model):
    creation_date = models.DateField(auto_created=True)
    name = models.CharField(max_length=500)
    summ = models.FloatField(max_length=500, null=False)
    description = models.CharField(max_length=500)
    plan = models.FloatField(max_length=500)
    permanent_income = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

    def __str__(self):
        return f'{self.name} {self.creation_date}'


class CategoryCost(models.Model):
    name = models.CharField(max_length=125)
    plan = models.FloatField()
    description = models.CharField(max_length=500)


class Costs(models.Model):
    '''
    Таблица расходы
    '''
    creation_date = models.DateField(auto_created=True)
    name = models.CharField(max_length=125)
    summ = models.FloatField()
    description = models.CharField(max_length=500)
    plan = models.FloatField()
    permanent_cost = models.FloatField()
    bound_cost = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    category_cost = models.ForeignKey(CategoryCost, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return f'{self.name} {self.creation_date}'


class Budget(models.Model):
    '''
    mtm таблица. Соединяет Доходы и расходы
    '''
    incomes = models.ForeignKey(Incomes, on_delete=models.CASCADE)
    costs = models.ForeignKey(Costs, on_delete=models.CASCADE)


class User(models.Model):
    '''
    Модель пользователя
    '''
    first_name = models.CharField(max_length=125)
    second_name = models.CharField(max_length=125)
    surname = models.CharField(max_length=125)
    creation_date = models.DateField(auto_created=True)
    avatar = models.ImageField('Аватар', upload_to='avatars')  # todo точно рассмотреть загрузку аватаров. Доделать присвоение имени и размеры
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12, unique=True)  # todo настроить параметаризатор для телефонов
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, default=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.surname}'
