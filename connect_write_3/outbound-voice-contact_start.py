#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-outbound-voice-contact.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # destination-phone-number : The phone number of the customer, in E.164 format.
    # contact-flow-id : The identifier of the contact flow for the outbound call. To see the ContactFlowId in the Amazon Connect console user interface, on the navigation menu go to Routing , Contact Flows . Choose the contact flow. On the contact flow page, under the name of the contact flow, choose Show additional flow information . The ContactFlowId is the last part of the ARN, shown here in bold:
arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/846ec553-a005-41c0-8341-xxxxxxxxxxxx
    # instance-id : The identifier of the Amazon Connect instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "start-outbound-voice-contact", "destination-phone-number", "contact-flow-id", "instance-id", add_option_dict)
