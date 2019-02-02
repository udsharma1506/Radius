from Agentdesks.models import User, Search, Property
import pandas as pd

def create_properties_bulk():

	df = pd.read_csv("HoustonData.csv")
	property_list = []
	for i in range(df.shape[0]):
		number_of_bedrooms = int(df.loc[i,'bedrooms_count'])
		data = {
			"name":df.loc[i,'title'],
			"location":"NONE",
			"street":"NONE",
			"city":df.loc[i,'city'],
			"country":"USA",
			"user":user,
			"latitude":df.loc[i,'latitude'],
			"longitude":df.loc[i,'longitude'],
			"price":float(str(df.loc[i,'average_rate_per_night'].replace("$","")) + "000"),
			"number_of_bedrooms":number_of_bedrooms,
			"number_of_bathrooms":random.randint(0,number_of_bedrooms),
			"descriptions":df.loc[i,"description"]
		}
		property_list.append(Property(**data))

	Property.objects.bulk_creat(property_list)

def creating_user(name = "Udit Sharma",contact_info = "9801213434", mail_id = "abc@xyz.com"):

	user = User(name = name,contact_info = contact_info, mail_id = mail_id)
	user.save()
	print "User Id is %s" %(user.pk)
	return user

def create_property(name, location, city, country, user_id, latitude, longitude, number_of_bedrooms, number_of_bathrooms):

		data = {
			"name":name,
			"location":location,
			"street":None,
			"city":city,
			"country":country,
			"user":user_id,
			"latitude":latitude,
			"longitude":longitude,
			"price":price,
			"number_of_bedrooms":number_of_bedrooms,
			"number_of_bathrooms":number_of_bathrooms,
			"descriptions":None
		}

		proprty = Property(**data)
		proprty.save()
		print "Property Id is %s" %(proprty.pk)

def Search_requirements(user_id, city, country, latitude, longitude, max_budget = 0, max_bedrooms= 0, max_bathrooms = 0,
						min_budget = 0, min_bedrooms = 0, min_bathrooms = 0):

	search = Search(user = user_id, city = city,
			country = country, latitude = latitude,
			longitude = longitude, min_budget = min_budget, max_budget= max_budget,
			min_bedrooms = min_bedrooms, max_bedrooms = max_bedrooms, min_bathrooms = min_bathrooms, 
			max_bathrooms = max_bathrooms)

	search.save()
	print "search Id is %s" %(search.pk)
	return search

