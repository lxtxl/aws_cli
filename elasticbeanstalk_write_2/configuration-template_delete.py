#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-configuration-template.html
if __name__ == '__main__':
    """
	create-configuration-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-configuration-template.html
	update-configuration-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-configuration-template.html
    """

    parameter_display_string = """
    # application-name : The name of the application to delete the configuration template from.
    # template-name : The name of the configuration template to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticbeanstalk", "delete-configuration-template", "application-name", "template-name", add_option_dict)
