#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/associate-targets-with-job.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # targets : A list of thing group ARNs that define the targets of the job.
(string)
    # job-id : The unique identifier you assigned to this job when it was created.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "associate-targets-with-job", "targets", "job-id", add_option_dict)
