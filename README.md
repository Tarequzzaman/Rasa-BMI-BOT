<h3>Rasa Bangla chat Bot</h3>

<p>For Rasa installation on your system please visit  <a href="https://rasa.com/docs/rasa/user-guide/installation/">here</a></p>


<p>The main goal of this project is create a Bengali conversational chatbot using Rasa</p>
<h2>custom response</h2>

Custom response is one of the feature of Rasa ai

To enable this use follow the steps:




1.add action to domain.yml

```
actions:
.
.
.
- action_hello_world
.
.
.
```

2. Enable endpoints.yml


```
action_endpoint:
 url: "http://localhost:5055/webhook"
```

3. Edit action.py



``` python
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
```



4. for installation python sdk for custom action go <a href="https://rasa.com/docs/rasa/api/rasa-sdk/#custom-action-example">here</a>

Install Sdk using: 
```
pip install rasa-sdk
```

rasa run actions
```
for run custom action
```
