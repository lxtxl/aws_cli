#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/disassociate-environment-operations-role.html
if __name__ == '__main__':
    """
	associate-environment-operations-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/associate-environment-operations-role.html
    """

    parameter_display_string = """
    # environment-name : The name of the environment from which to disassociate the operations role.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticbeanstalk", "disassociate-environment-operations-role", "environment-name", add_option_dict)





