#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-events/put-events.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # tracking-id : The tracking ID for the event. The ID is generated by a call to the CreateEventTracker API.
    # session-id : The session ID associated with the userâs visit. Your application generates the sessionId when a user first visits your website or uses your application. Amazon Personalize uses the sessionId to associate events with the user before they log in. For more information see  event-record-api .
    # event-list : A list of event data from the session.
(structure)

Represents user interaction event information sent using the PutEvents API.
eventId -> (string)

An ID associated with the event. If an event ID is not provided, Amazon Personalize generates a unique ID for the event. An event ID is not used as an input to the model. Amazon Personalize uses the event ID to distinquish unique events. Any subsequent events after the first with the same event ID are not used in model training.

eventType -> (string)

The type of event, such as click or download. This property corresponds to the EVENT_TYPE field of your Interactions schema and depends on the types of events you are tracking.

eventValue -> (float)

The event value that corresponds to the EVENT_VALUE field of the Interactions schema.

itemId -> (string)

The item ID key that corresponds to the ITEM_ID field of the Interactions schema.

properties -> (string)

A string map of event-specific data that you might choose to record. For example, if a user rates a movie on your site, other than movie ID (itemId ) and rating (eventValue ) , you might also send the number of movie ratings made by the user.
Each item in the map consists of a key-value pair. For example,

{"numberOfRatings": "12"}

The keys use camel case names that match the fields in the Interactions schema. In the above example, the numberOfRatings would match the âNUMBER_OF_RATINGSâ field defined in the Interactions schema.

sentAt -> (timestamp)

The timestamp (in Unix time) on the client side when the event occurred.

recommendationId -> (string)

The ID of the recommendation.

impression -> (list)

A list of item IDs that represents the sequence of items you have shown the user. For example, ["itemId1", "itemId2", "itemId3"] .
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("personalize-events", "put-events", "tracking-id", "session-id", "event-list", add_option_dict)
