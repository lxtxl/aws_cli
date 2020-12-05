#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/request-environment-info.html
if __name__ == '__main__':
    """
	retrieve-environment-info : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/retrieve-environment-info.html
    """

    parameter_display_string = """
    # info-type : The type of information to request.
Possible values:

tail
bundle
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticbeanstalk", "request-environment-info", "info-type", add_option_dict)





