#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html
if __name__ == '__main__':
    """
	delete-distribution-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-distribution-configuration.html
	get-distribution-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-distribution-configuration.html
	list-distribution-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-distribution-configurations.html
	update-distribution-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html
    """

    parameter_display_string = """
    # name : The name of the distribution configuration.
    # distributions : The distributions of the distribution configuration.
(structure)

Defines the settings for a specific Region.
region -> (string)

The target Region.

amiDistributionConfiguration -> (structure)

The specific AMI settings (for example, launch permissions, AMI tags).
name -> (string)

The name of the distribution configuration.

description -> (string)

The description of the distribution configuration. Minimum and maximum length are in characters.

targetAccountIds -> (list)

The ID of an account to which you want to distribute an image.
(string)

amiTags -> (map)

The tags to apply to AMIs distributed to this Region.
key -> (string)
value -> (string)

kmsKeyId -> (string)

The KMS key identifier used to encrypt the distributed image.

launchPermission -> (structure)

Launch permissions can be used to configure which AWS accounts can use the AMI to launch instances.
userIds -> (list)

The AWS account ID.
(string)

userGroups -> (list)

The name of the group.
(string)



licenseConfigurationArns -> (list)

The License Manager Configuration to associate with the AMI in the specified Region.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("imagebuilder", "create-distribution-configuration", "name", "distributions", add_option_dict)
