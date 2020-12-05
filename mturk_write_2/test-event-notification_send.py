#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/send-test-event-notification.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # notification : 
    # test-event-type : The event to simulate to test the notification specification. This event is included in the test message even if the notification specification does not include the event type. The notification specification does not filter out the test event.
Possible values:

AssignmentAccepted
AssignmentAbandoned
AssignmentReturned
AssignmentSubmitted
AssignmentRejected
AssignmentApproved
HITCreated
HITExpired
HITReviewable
HITExtended
HITDisposed
Ping
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mturk", "send-test-event-notification", "notification", "test-event-type", add_option_dict)
