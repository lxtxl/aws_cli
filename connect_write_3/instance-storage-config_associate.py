#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-instance-storage-config.html
if __name__ == '__main__':
    """
	describe-instance-storage-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance-storage-config.html
	disassociate-instance-storage-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-instance-storage-config.html
	list-instance-storage-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-instance-storage-configs.html
	update-instance-storage-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-instance-storage-config.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # resource-type : A valid resource type.
Possible values:

CHAT_TRANSCRIPTS
CALL_RECORDINGS
SCHEDULED_REPORTS
MEDIA_STREAMS
CONTACT_TRACE_RECORDS
AGENT_EVENTS
    # storage-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "associate-instance-storage-config", "instance-id", "resource-type", "storage-config", add_option_dict)
