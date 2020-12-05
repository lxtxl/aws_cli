#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-events/put-users.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # dataset-arn : The Amazon Resource Number (ARN) of the Users dataset you are adding the user or users to.
    # users : A list of user data.
(structure)

Represents user metadata added to a Users dataset using the PutUsers API.
userId -> (string)

The ID associated with the user.

properties -> (string)

A string map of user-specific metadata. Each element in the map consists of a key-value pair. For example,

{"numberOfVideosWatched": "45"}

The keys use camel case names that match the fields in the Users schema. In the above example, the numberOfVideosWatched would match the âNUMBER_OF_VIDEOS_WATCHEDâ field defined in the Users schema.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("personalize-events", "put-users", "dataset-arn", "users", add_option_dict)
