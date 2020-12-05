#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/associate-proactive-engagement-details.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # emergency-contact-list : A list of email addresses and phone numbers that the DDoS Response Team (DRT) can use to contact you for escalations to the DRT and to initiate proactive customer support.
To enable proactive engagement, the contact list must include at least one phone number.

Note
The contacts that you provide here replace any contacts that were already defined. If you already have contacts defined and want to use them, retrieve the list using DescribeEmergencyContactSettings and then provide it here.

(structure)

Contact information that the DRT can use to contact you if you have proactive engagement enabled, for escalations to the DRT and to initiate proactive customer support.
EmailAddress -> (string)

The email address for the contact.

PhoneNumber -> (string)

The phone number for the contact.

ContactNotes -> (string)

Additional notes regarding the contact.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("shield", "associate-proactive-engagement-details", "emergency-contact-list", add_option_dict)





