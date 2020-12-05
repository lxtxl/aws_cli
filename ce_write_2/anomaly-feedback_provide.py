#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/provide-anomaly-feedback.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # anomaly-id : A cost anomaly ID.
    # feedback : Describes whether the cost anomaly was a planned activity or you considered it an anomaly.
Possible values:

YES
NO
PLANNED_ACTIVITY
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ce", "provide-anomaly-feedback", "anomaly-id", "feedback", add_option_dict)
