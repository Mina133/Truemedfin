from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    package = models.IntegerField()
    number_of_pieces = models.IntegerField()

    def price(self):
        if self.number_of_pieces == 0 or self.package == 0:
            return 0
        return self.package / self.number_of_pieces

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item)

    def list_price(self):
        items = self.items.all()
        return sum(item.price() for item in items)

    def __str__(self):
        return self.name


class WorkingHours(models.Model):
    hours_per_day = models.IntegerField()
    days_per_week = models.IntegerField()

    def hours_per_week(self):
        return self.hours_per_day * self.days_per_week  # 5 * 6 = 30 (based on image)

    def hours_per_month(self):
        return self.hours_per_week() * 4  # 30 * 4 = 120

    def hours_per_year(self):
        return self.hours_per_month() * 12  # 120 * 12 = 1440

    def days_per_month(self):
        return self.days_per_week * 4

    def days_per_year(self):
        return self.days_per_month() * 12


class Depreciation(models.Model):
    investment_cost = models.IntegerField()
    number_of_years = models.IntegerField()

    def depreciation_per_year(self):
        return self.investment_cost / self.number_of_years  # Based on image: 140000/year

    def depreciation_per_month(self):
        return self.depreciation_per_year() / 12  # 140000 / 12 = 11667

    def depreciation_per_day(self, working_hours_instance):
        days_per_month = working_hours_instance.days_per_month()
        return self.depreciation_per_month() / days_per_month  # Daily depreciation = 486 (from image)

    def depreciation_per_hour(self, working_hours_instance):
        hours_per_month = working_hours_instance.hours_per_month()
        return self.depreciation_per_month() / hours_per_month  # 11667 / 120 = 97


class FixedOperationalCost(models.Model):
    rent = models.IntegerField()
    routine_marketing = models.IntegerField()
    bills = models.IntegerField()
    secretary_and_assistant = models.IntegerField()
    doctor_salaries = models.IntegerField()

    def fixed_operational_cost_per_month(self):
        return (
            self.rent +
            self.routine_marketing +
            self.bills +
            self.secretary_and_assistant +
            self.doctor_salaries
        )  # Summing monthly costs: Rent, marketing, salaries, bills

    def fixed_operational_cost_per_hour(self, working_hours_instance):
        hours_per_month = working_hours_instance.hours_per_month()  # Use 120 hours/month from image
        return self.fixed_operational_cost_per_month() / hours_per_month  # 43700 / 120 = 364


def total_operational_cost_per_hour(working_hours_instance, fixed_cost_instance, depreciation_instance):
    """
    Calculate the total operational cost per hour by summing fixed costs and depreciation costs.
    """
    fixed_cost_hourly = fixed_cost_instance.fixed_operational_cost_per_hour(working_hours_instance)
    depreciation_hourly = depreciation_instance.depreciation_per_hour(working_hours_instance)
    return fixed_cost_hourly + depreciation_hourly  


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    specific_items = models.ManyToManyField(Item, related_name='specialization_items')
    specific_lists = models.ManyToManyField(List, related_name='specialization_lists')

    def cost_per_patient(self, working_hours, fixed_cost, depreciation):
        """
        Calculate the cost per patient based on items, lists, and operational costs.
        """
        total_items_cost = sum(item.price() for item in self.specific_items.all())
        total_lists_cost = sum(lst.list_price() for lst in self.specific_lists.all())
        hourly_cost = total_operational_cost_per_hour(working_hours, fixed_cost, depreciation)
        return total_items_cost + total_lists_cost + (hourly_cost*0.5)

    def service_cost(self, working_hours, fixed_cost, depreciation):
        """
        Calculate the service cost as 35% of cost per patient.
        """
        cost_per_patient = self.cost_per_patient(working_hours, fixed_cost, depreciation)
        return cost_per_patient * 1.35  # 100% + 35%

    def __str__(self):
        return self.name

