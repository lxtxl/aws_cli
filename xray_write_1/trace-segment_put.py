#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-trace-segments.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # trace-segment-documents : A string containing a JSON document defining one or more segments or subsegments.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("xray", "put-trace-segments", "trace-segment-documents", add_option_dict)





