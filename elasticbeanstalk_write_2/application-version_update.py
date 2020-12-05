#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-application-version.html
if __name__ == '__main__':
    """
	create-application-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-application-version.html
	delete-application-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-application-version.html
	describe-application-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-application-versions.html
    """

    parameter_display_string = """
    # application-name : The name of the application associated with this version.
If no application is found with this name, UpdateApplication returns an InvalidParameterValue error.
    # version-label : The name of the version to update.
If no application version is found with this label, UpdateApplication returns an InvalidParameterValue error.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticbeanstalk", "update-application-version", "application-name", "version-label", add_option_dict)
