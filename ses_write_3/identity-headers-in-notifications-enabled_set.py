#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/set-identity-headers-in-notifications-enabled.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # identity : The identity for which to enable or disable headers in notifications. Examples: user@example.com , example.com .
    # notification-type : The notification type for which to enable or disable headers in notifications.
Possible values:

Bounce
Complaint
Delivery
    # enabled | --no-enabled : Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of true specifies that Amazon SES will include headers in notifications, and a value of false specifies that Amazon SES will not include headers in notifications.
This value can only be set when NotificationType is already set to use a particular Amazon SNS topic.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ses", "set-identity-headers-in-notifications-enabled", "identity", "notification-type", "enabled | --no-enabled", add_option_dict)
