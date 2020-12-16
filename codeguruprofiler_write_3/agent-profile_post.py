#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/post-agent-profile.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # agent-profile : 
    # content-type : The format of the submitted profiling data. The format maps to the Accept and Content-Type headers of the HTTP request. You can specify one of the following: or the default .

<ul> <li> <p> <code>application/json</code> â standard JSON format </p> </li> <li> <p> <code>application/x-amzn-ion</code> â the Amazon Ion data format. For more information, see <a href="http://amzn.github.io/ion-docs/">Amazon Ion</a>. </p> </li> </ul>
    # profiling-group-name : The name of the profiling group with the aggregated profile that receives the submitted profiling data.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codeguruprofiler", "post-agent-profile", "agent-profile", "content-type", "profiling-group-name", add_option_dict)
