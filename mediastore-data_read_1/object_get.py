#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/get-object.html
if __name__ == '__main__':
    """
	delete-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/delete-object.html
	describe-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/describe-object.html
	put-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/put-object.html
    """

    parameter_display_string = """
    # path : The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>
For example, to upload the file mlaw.avi to the folder path premium\canada in the container movies , enter the path premium/canada/mlaw.avi .
Do not include the container name in this path.
If the path includes any folders that donât exist yet, the service creates them. For example, suppose you have an existing premium/usa subfolder. If you specify premium/canada , the service creates a canada subfolder in the premium folder. You then have two subfolders, usa and canada , in the premium folder.
There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.
For more information about folders and how they exist in a container, see the AWS Elemental MediaStore User Guide .
The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("mediastore-data", "get-object", "path", add_option_dict)