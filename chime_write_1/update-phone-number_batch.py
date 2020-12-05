#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-update-phone-number.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # update-phone-number-request-items : The request containing the phone number IDs and product types or calling names to update.
(structure)

The phone number ID, product type, or calling name fields to update, used with the  BatchUpdatePhoneNumber and  UpdatePhoneNumber actions.
PhoneNumberId -> (string)

The phone number ID to update.

ProductType -> (string)

The product type to update.

CallingName -> (string)

The outbound calling name to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "batch-update-phone-number", "update-phone-number-request-items", add_option_dict)





