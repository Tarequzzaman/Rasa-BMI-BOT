# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ent = tracker.latest_message
        print(ent)

        dispatcher.utter_message(text="Hello World!")
        return []








class WeightSET(Action):
    def name(self) -> Text:
        return "action_set_weight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
       
           tracker.get_slot("weight")
        except:
            dispatcher.utter_message(text="Error Occur!")

        dispatcher.utter_message(text="Weight set")
        return []

class HeightSET(Action):
    def name(self) -> Text:
        return "action_set_height"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            tracker.get_slot("height")
        except:
            dispatcher.utter_message(text="Error Occur!")
        dispatcher.utter_message(text="Height set")
        return []


def convert_inch_to_meter(height):
    return height * 0.3048

def bmi_calculation(weight, height):
    return float(weight)/(height*height)


def get_bmi_status(bmi):
    if bmi < 15:
       return  "Very severely underweight"
    elif bmi >= 15 and bmi <16:
        return "Severely underweight"
    elif bmi >=16 and bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25: 
        return "Normal (healthy weight)"
    elif  bmi >= 25 and bmi <30:
        return "Overweight"
    elif bmi>= 30 and bmi <35:
        return "Moderately obese"
    elif bmi >= 35 and bmi<40:
        return "Severely obese"
    else:
        return "Very severely obese"


class CalculeteBMI(Action):
    def name(self) -> Text:
        return "action_calculate_bmi"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            height =  float(tracker.get_slot("height"))
            print(height)
            height = convert_inch_to_meter(height)
       
            weight = float(tracker.get_slot("weight"))
            print(weight)
            bmi = bmi_calculation(weight, height)
            bmi_status = get_bmi_status(bmi)
            dispatcher.utter_message(text="Your BMI is: "+ str(round(bmi, 2))+" and it is "+ bmi_status)
        except:
            dispatcher.utter_message(text="Error Occur!")
            return []

