#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-environment.html
if __name__ == '__main__':
    """
	compose-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/compose-environments.html
	describe-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-environments.html
	rebuild-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/rebuild-environment.html
	terminate-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/terminate-environment.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-environment.html
    """

    parameter_display_string = """
    # application-name : The name of the application that is associated with this environment.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticbeanstalk", "create-environment", "application-name", add_option_dict)





