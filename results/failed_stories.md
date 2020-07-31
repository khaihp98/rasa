## happy path 1 (/tmp/tmpwa4stn2j/455b03860cc2435388a2bbb300831bfb_conversation_tests.md)
* greet: hello there!   <!-- predicted: greeting: hello there! -->
    - utter_greet   <!-- predicted: action_chitchat -->
* mood_great: amazing   <!-- predicted: greeting: amazing -->
    - utter_happy   <!-- predicted: action_chitchat -->


## happy path 2 (/tmp/tmpwa4stn2j/455b03860cc2435388a2bbb300831bfb_conversation_tests.md)
* greet: hello there!   <!-- predicted: greeting: hello there! -->
    - utter_greet   <!-- predicted: action_chitchat -->
* mood_great: amazing   <!-- predicted: greeting: amazing -->
    - utter_happy   <!-- predicted: action_chitchat -->
* goodbye: bye-bye!   <!-- predicted: bye: bye-bye! -->
    - utter_goodbye   <!-- predicted: action_chitchat -->


## sad path 1 (/tmp/tmpwa4stn2j/455b03860cc2435388a2bbb300831bfb_conversation_tests.md)
* greet: hello   <!-- predicted: greeting: hello -->
    - utter_greet   <!-- predicted: action_chitchat -->
* mood_unhappy: not good   <!-- predicted: bye: not good -->
    - utter_cheer_up   <!-- predicted: action_chitchat -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: bye: yes -->
    - utter_happy   <!-- predicted: action_chitchat -->


## sad path 2 (/tmp/tmpwa4stn2j/455b03860cc2435388a2bbb300831bfb_conversation_tests.md)
* greet: hello   <!-- predicted: greeting: hello -->
    - utter_greet   <!-- predicted: action_chitchat -->
* mood_unhappy: not good   <!-- predicted: bye: not good -->
    - utter_cheer_up   <!-- predicted: action_chitchat -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: bye: not really -->
    - utter_goodbye   <!-- predicted: action_chitchat -->


## sad path 3 (/tmp/tmpwa4stn2j/455b03860cc2435388a2bbb300831bfb_conversation_tests.md)
* greet: hi   <!-- predicted: greeting: hi -->
    - utter_greet   <!-- predicted: action_chitchat -->
* mood_unhappy: very terrible   <!-- predicted: greeting: very terrible -->
    - utter_cheer_up   <!-- predicted: action_chitchat -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: greeting: no -->
    - utter_goodbye   <!-- predicted: action_chitchat -->


## say goodbye (/tmp/tmpwa4stn2j/455b03860cc2435388a2bbb300831bfb_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: bye: bye-bye! -->
    - utter_goodbye   <!-- predicted: action_chitchat -->


## bot challenge (/tmp/tmpwa4stn2j/455b03860cc2435388a2bbb300831bfb_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: ask_love_together: are you a bot? -->
    - utter_iamabot   <!-- predicted: action_chitchat -->


