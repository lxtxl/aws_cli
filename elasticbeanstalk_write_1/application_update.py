#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-application.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-application.html
	delete-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-application.html
	describe-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-applications.html
    """

    parameter_display_string = """
    # application-name : The name of the application to update. If no such application is found, UpdateApplication returns an InvalidParameterValue error.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticbeanstalk", "update-application", "application-name", add_option_dict)





