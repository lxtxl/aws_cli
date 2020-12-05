#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-collection.html
if __name__ == '__main__':
    """
	delete-collection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-collection.html
	describe-collection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-collection.html
	list-collections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-collections.html
    """

    parameter_display_string = """
    # collection-id : ID for the collection that you are creating.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rekognition", "create-collection", "collection-id", add_option_dict)





