#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-settings.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-pool-id : The ID of the user pool that contains the user that you are setting options for.
    # username : The user name of the user that you are setting options for.
    # mfa-options : You can use this parameter only to set an SMS configuration that uses SMS for delivery.
(structure)


This data type is no longer supported. You can use it only for SMS MFA configurations. You canât use it for TOTP software token MFA configurations.

DeliveryMedium -> (string)

The delivery medium to send the MFA code. You can use this parameter to set only the SMS delivery medium value.

AttributeName -> (string)

The attribute name of the MFA option type. The only valid value is phone_number .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "admin-set-user-settings", "user-pool-id", "username", "mfa-options", add_option_dict)
