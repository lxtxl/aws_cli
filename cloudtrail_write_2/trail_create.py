#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-trail.html
if __name__ == '__main__':
    """
	delete-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-trail.html
	describe-trails : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/describe-trails.html
	get-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail.html
	list-trails : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-trails.html
	update-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-trail.html
    """

    parameter_display_string = """
    # name : Specifies the name of the trail. The name must meet the following requirements:

Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
Start with a letter or number, and end with a letter or number
Be between 3 and 128 characters
Have no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.
Not be in IP address format (for example, 192.168.5.4)
    # s3-bucket-name : Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudtrail", "create-trail", "name", "s3-bucket-name", add_option_dict)
