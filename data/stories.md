<!-- ## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy -->


## only greet
* greet
   - utter_greet

## ask Bmi
* BMI_mapbo
   - utter_ask_weight
* my_weight
   - action_set_weight
   - utter_ask_height
* my_height
  - action_set_height
  - action_calculate_bmi

  

  
## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## matha betha detect
* greet
  - utter_greet
* matha_betha
  - utter_ask_about_headac
* headec_left
  - utter_headac_solution

## custom_response
* greet
  - utter_greet
* mood_great
  - action_hello_world




## New Story

* greet
    - utter_greet
* matha_betha
    - utter_ask_about_headac
* headec_left
    - utter_headac_solution
* goodbye
    - utter_goodbye
