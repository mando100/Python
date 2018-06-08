from django.db import models

# Create your models here.
class Campaign(models.Model):
	campaign_id = models.IntegerField(default=0,primary_key=True)
	name = models.CharField(max_length=200)
	cost = models.FloatField()
	revenue = models.FloatField()
	currency = models.CharField(max_length=3)
	conversions = models.IntegerField()

	def __str__(self):
		return self.name

	def getCampaignId (self):
		return self.campaign_id

	def getCost (self):
		return self.cost

	def getRevenue (self):
		return self.revenue

	def getCurrency (self):
		return self.currency

	def getConversions (self):
		return self.conversions