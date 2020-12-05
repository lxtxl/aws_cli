#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/tag-stream.html
if __name__ == '__main__':
    """
	create-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/create-stream.html
	delete-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/delete-stream.html
	describe-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/describe-stream.html
	list-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/list-streams.html
	untag-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/untag-stream.html
	update-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/update-stream.html
    """

    parameter_display_string = """
    # tags : A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).
key -> (string)
value -> (string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kinesisvideo", "tag-stream", "tags", add_option_dict)





