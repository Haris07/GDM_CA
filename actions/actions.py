# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
from rasa_sdk.types import DomainDict


class ActionCalculateDose(Action):

    def name(self) -> Text:
        return "action_calculate_dose"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slot_weight = int(tracker.get_slot('weight'))
        slot_trimester = tracker.get_slot('trimester')

        print(slot_weight)
        print(slot_trimester)

        slot_dose = 0.0

        if slot_weight > 0:
            if slot_trimester == 'first' or '1st':
                slot_dose = 0.7 * slot_weight
            elif slot_trimester == 'second' or '2nd':
                slot_dose = 0.8 * slot_weight
            elif slot_trimester == 'third' or '3rd':
                slot_dose = 0.9 * slot_weight


        dispatcher.utter_message(response="utter_user_dose", weight=slot_weight, trimester=slot_trimester, dose=slot_dose)    

        
        # dispatcher.utter_message(text="Hello World!")
                
        # return [SlotSet("weight", None), SlotSet("trimester", None)]
        return [Restarted()]

class ActionRestart(Action):

  def name(self) -> Text:
      return "action_restart"

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:

      # custom behavior
    dispatcher.utter_message(text="The bot restarts now...")

    return [Restarted()]

# from typing import Text, List, Any, Dict


# class ValidateUserInfoForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_user_info_form"

#     def validate_trimester(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate trimester value."""

        
#         if slot_value.lower() in self.cuisine_db():
#             # validation succeeded, set the value of the "cuisine" slot to value
#             return {"cuisine": slot_value}
#         else:
#             # validation failed, set this slot to None so that the
#             # user will be asked for the slot again
#             return {"cuisine": None}