#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-instance-attribute.html
if __name__ == '__main__':
    """
	describe-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance-attribute.html
	list-instance-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-instance-attributes.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # attribute-type : The type of attribute.
Possible values:

INBOUND_CALLS
OUTBOUND_CALLS
CONTACTFLOW_LOGS
CONTACT_LENS
AUTO_RESOLVE_BEST_VOICES
USE_CUSTOM_TTS_VOICES
EARLY_MEDIA
    # value : The value for the attribute. Maximum character limit is 100.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "update-instance-attribute", "instance-id", "attribute-type", "value", add_option_dict)
