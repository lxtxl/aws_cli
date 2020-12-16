#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance-attribute.html
if __name__ == '__main__':
    """
	list-instance-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-instance-attributes.html
	update-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-instance-attribute.html
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
    """

    execute_two_parameter("connect", "describe-instance-attribute", "instance-id", "attribute-type", parameter_display_string)