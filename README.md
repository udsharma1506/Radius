# Radius

This is a Django Project having an APP called AgentDesks. AgenetDesks app has views ( where APIs logic is written,
models where models used is described and scripts where the scripts to update the data is there ).

Agentdesk has 3 models: User, Search and Property

User has 3 fields: name, contact_info, mail_id. This is used to store user level basic information

Search has 12 fields to store the basic data of the search doing by the user to find the property. 
Each search has a ForeignKey relation to the user field

Propery table contains the basis property data.

Clone the repo, and run

Python manage.pt shell

from Agentdesks.scripts import *

#create user
creating_user("Jack","1234324423531","jack21@gmail.com)

#create searchr requirements entered by the user
search_requirements(user_id = 1, city = "Houston",country = "USA", latitude = 29.7823356, longitude = -95.3655487,
  min_budget = 20000, max_budget = 700000, min_bedrooms = 0, max_bedrooms = 2, min_bathrooms = 1, max_bathrooms = 2)

I have already written the script to bulk create the Properties used in this kaggel Challenge

If you want to create more properties, use giving the mentioned inputs:
create_property(name, location, city, country, user_id, latitude, longitude, number_of_bedrooms, number_of_bathrooms)


Usage:

After feeling all the data required to search for the properties, run the code at PORT: 8008 ( I used this )

python manage.py runserver 8008

To get the matched property for the user, use API

http://127.0.0.1:8008/agentdesks/get-properties/?user=2 
where user is the user ID for whom you want the results.

To get the matched user for the property, use API

http://127.0.0.1:8008/agentdesks/get-requirements/?property_id=1500
where property_id is the property Id for whom we want users interested on





