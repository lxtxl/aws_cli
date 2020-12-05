#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-tags-for-resource.html
if __name__ == '__main__':
    """
	list-tags-for-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-tags-for-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resouce to be updated.
Must be the ARN of an Elastic Beanstalk resource.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticbeanstalk", "update-tags-for-resource", "resource-arn", add_option_dict)





