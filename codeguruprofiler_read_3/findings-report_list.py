#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-findings-reports.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # end-time : Optionally specifies that log files delivered on or before the specified UTC timestamp value will be validated. The default value is the current time. Example: â2015-01-08T12:31:41Zâ.
    # profiling-group-name : The name of the profiling group from which to search for analysis data.
    """

    execute_two_parameter("codeguruprofiler", "list-findings-reports", "end-time", "profiling-group-name", parameter_display_string)