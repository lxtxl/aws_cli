#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_process

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rb.html
if __name__ == '__main__':
    parameter_display_string = """
    # bucket : Specifies the bucket being deleted.
    """
    add_option_dict = {}

    parameter_num = len(sys.argv)

    if parameter_num != 3:
        print("config value is not exist")
        print("Usage: python {} <config> <bucket_name>".format(sys.argv[0]))
        print(parameter_display_string)
        sys.exit(0)

    profile_name = sys.argv[1]
    unique_value = sys.argv[2]
    answer = input("Enter yes or no: ")
    if answer == "yes":
        add_parameter_list = []
        replace_unique_value = "s3://" + unique_value
        add_parameter_list.append(replace_unique_value)
        add_parameter_list.append("--force")
        execute_process(profile_name, "s3", "rb", add_parameter_list)
    else:
        sys.exit()





