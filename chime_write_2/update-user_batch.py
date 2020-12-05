#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-update-user.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # update-user-request-items : The request containing the user IDs and details to update.
(structure)

The user ID and user fields to update, used with the  BatchUpdateUser action.
UserId -> (string)

The user ID.

LicenseType -> (string)

The user license type.

UserType -> (string)

The user type.

AlexaForBusinessMetadata -> (structure)

The Alexa for Business metadata.
IsAlexaForBusinessEnabled -> (boolean)

Starts or stops Alexa for Business.

AlexaForBusinessRoomArn -> (string)

The ARN of the room resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "batch-update-user", "account-id", "update-user-request-items", add_option_dict)
