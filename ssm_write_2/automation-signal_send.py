#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/send-automation-signal.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # automation-execution-id : The unique identifier for an existing Automation execution that you want to send the signal to.
    # signal-type : The type of signal to send to an Automation execution.
Possible values:

Approve
Reject
StartStep
StopStep
Resume
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "send-automation-signal", "automation-execution-id", "signal-type", add_option_dict)
