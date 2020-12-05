#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-configuration-template.html
if __name__ == '__main__':
    """
	delete-configuration-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-configuration-template.html
	update-configuration-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-configuration-template.html
    """

    parameter_display_string = """
    # application-name : The name of the Elastic Beanstalk application to associate with this configuration template.
    # template-name : The name of the configuration template.
Constraint: This name must be unique per application.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticbeanstalk", "create-configuration-template", "application-name", "template-name", add_option_dict)
