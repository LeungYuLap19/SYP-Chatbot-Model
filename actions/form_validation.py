from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict

class ValidateCheckFlightsForm(FormValidationAction):
  def name(self) -> Text:
    return 'validate_check_flights_form'

  async def validate(
    self, 
    domain_slots: List[Text], 
    dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: DomainDict
  ) -> List[Text]:
    # Retrieve all slots
    departure_city = tracker.get_slot("departure_city")
    destination_city = tracker.get_slot("destination_city")
    departure_airport = tracker.get_slot("departure_airport")
    destination_airport = tracker.get_slot("destination_airport")
    flight_type = tracker.get_slot("flight_type")
    departure_date = tracker.get_slot("departure_date")
    return_date = tracker.get_slot("return_date")

    validated_slots = {}

    # implement form checking logics
    if departure_airport and destination_airport:
      validated_slots["departure_airport"] = departure_airport
      validated_slots["destination_airport"] = destination_airport
      validated_slots["departure_city"] = None 
      validated_slots["destination_city"] = None
    elif departure_city and destination_city:
      validated_slots["departure_city"] = departure_city
      validated_slots["destination_city"] = destination_city
      validated_slots["departure_airport"] = None  
      validated_slots["destination_airport"] = None
    else:
      validated_slots["departure_city"] = None
      validated_slots["destination_city"] = None
      validated_slots["departure_airport"] = None
      validated_slots["destination_airport"] = None
      dispatcher.utter_message(text="Please provide both departure and destination cities or both airports.")

    if not flight_type:
      validated_slots["flight_type"] = None
      dispatcher.utter_message(text="Please specify if the flight is 'oneway' or 'return'.")
    else:
      validated_slots["flight_type"] = flight_type

    if not departure_date:
      validated_slots["departure_date"] = None
      dispatcher.utter_message(text="Please provide the departure date.")
    else:
      validated_slots["departure_date"] = departure_date

    if flight_type == "return" and not return_date:
      validated_slots["return_date"] = None
      dispatcher.utter_message(text="Please provide the return date.")
    elif flight_type == "oneway":
      validated_slots["return_date"] = None 
    else:
      validated_slots["return_date"] = return_date

    return validated_slots

class ValidateAskFlightStatusForm(FormValidationAction):
  def name(self) -> Text:
    return 'validate_ask_flight_status_form'

  async def validate_flight_number(
    self, 
    domain_slots: List[Text], 
    dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: DomainDict
  ) -> List[Text]:
    flight_number = tracker.get_slot("flight_number")

    if not flight_number:
      dispatcher.utter_message(text="Please provide your flight number.")
      return {"flight_number": None}

    return {"flight_number": flight_number}
  
class ValidateFindHotelsForm(FormValidationAction):
  def name(self) -> Text:
    return 'validate_find_hotels_form'
  
  async def validate(
    self, 
    domain_slots: List[Text], 
    dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: DomainDict
  ) -> List[Text]:
    resident_city = tracker.get_slot("resident_city")
    check_in_date = tracker.get_slot("check_in_date")
    check_out_date = tracker.get_slot("check_out_date")
    amenity = tracker.get_slot("amenity")

    validated_slots = {}

    if resident_city:
      validated_slots["resident_city"] = resident_city
    else:
      validated_slots["resident_city"] = None
      dispatcher.utter_message(text="Please provide a valid city of residence.")

    if check_in_date: 
      validated_slots["check_in_date"] = check_in_date
    else:
      validated_slots["check_in_date"] = None
      dispatcher.utter_message(text="Please provide a valid check-in date.")

    if check_out_date: 
      validated_slots["check_out_date"] = check_out_date
    else:
      validated_slots["check_out_date"] = None
      dispatcher.utter_message(text="Please provide a valid check-out date.")
    
    if amenity:
      validated_slots["amenity"] = amenity
    else:
      validated_slots["amenity"] = None

    return validated_slots
  
class ValidateTavelRecommendationsForm(FormValidationAction):
  def name(self) -> Text:
    return "validate_travel_recommendations_form"
  
  async def validate_travel_city(
    self, 
    domain_slots: List[Text], 
    dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: DomainDict
  ) -> List[Text]:
    travel_city = tracker.get_slot("travel_city")

    if not travel_city:
      dispatcher.utter_message(text="Please provide the city you want to travel.")
      return {"travel_city": None}

    return {"travel_city": travel_city}
  
class ValidateAskWeatherForm(FormValidationAction):
  def name(self) -> Text:
    return "validate_ask_weather_form"
  
  async def validate(
    self, 
    domain_slots: List[Text], 
    dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: DomainDict
  ) -> List[Text]:
    travel_city = tracker.get_slot("travel_city")
    forecast = tracker.get_slot("forecast")

    validated_slots = {}

    if travel_city:
      validated_slots["travel_city"] = travel_city
    else:
      validated_slots["travel_city"] = None
      dispatcher.utter_message(text="Please provide the city you want to travel.")

    if forecast:
      validated_slots["forecast"] = forecast
    else:
      validated_slots["forecast"] = None

    return validated_slots
  
class ValidateAskRestrictionsTipsForm(FormValidationAction):
  def name(self) -> Text:
    return "validate_ask_restrictions_tips_form"
  
  async def validate_country(
    self, 
    domain_slots: List[Text], 
    dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: DomainDict
  ) -> List[Text]:
    country = tracker.get_slot("country")

    if not country:
      dispatcher.utter_message(text="Please provide the country you want to enquire.")
      return {"country": None}
    
    return {"country": country}
  
class ValidateAskCurrencyExchangeForm(FormValidationAction):
  def name(self) -> Text:
    return "validate_ask_currency_exchange_form"
  
  async def validate(
    self, 
    domain_slots: List[Text], 
    dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: DomainDict
  ) -> List[Text]:
    amount = tracker.get_slot("amount")
    source_currency = tracker.get_slot("source_currency")
    target_currency = tracker.get_slot("target_currency")

    validated_slots = {}

    if amount:
      validated_slots["amount"] = amount
    else:
      validated_slots["amount"] = 1
    
    if source_currency:
      validated_slots["source_currency"] = source_currency
    else:
      validated_slots["source_currency"] = None
      dispatcher.utter_message(text="Please provide the source currency.")

    if target_currency:
      validated_slots["target_currency"] = target_currency
    else:
      validated_slots["target_currency"] = None
      dispatcher.utter_message(text="Please provide the target currency.")

    return validated_slots