#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-workspaces.html
if __name__ == '__main__':
    """
	describe-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces.html
	migrate-workspace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/migrate-workspace.html
	reboot-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/reboot-workspaces.html
	rebuild-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/rebuild-workspaces.html
	restore-workspace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/restore-workspace.html
	start-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/start-workspaces.html
	stop-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/stop-workspaces.html
	terminate-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/terminate-workspaces.html
    """

    parameter_display_string = """
    # workspaces : The WorkSpaces to create. You can specify up to 25 WorkSpaces.
(structure)

Describes the information used to create a WorkSpace.
DirectoryId -> (string)

The identifier of the AWS Directory Service directory for the WorkSpace. You can use  DescribeWorkspaceDirectories to list the available directories.

UserName -> (string)

The user name of the user for the WorkSpace. This user name must exist in the AWS Directory Service directory for the WorkSpace.

BundleId -> (string)

The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list the available bundles.

VolumeEncryptionKey -> (string)

The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.

UserVolumeEncryptionEnabled -> (boolean)

Indicates whether the data stored on the user volume is encrypted.

RootVolumeEncryptionEnabled -> (boolean)

Indicates whether the data stored on the root volume is encrypted.

WorkspaceProperties -> (structure)

The WorkSpace properties.
RunningMode -> (string)

The running mode. For more information, see Manage the WorkSpace Running Mode .

RunningModeAutoStopTimeoutInMinutes -> (integer)

The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.

RootVolumeSizeGib -> (integer)

The size of the root volume. For important information about how to modify the size of the root and user volumes, see Modify a WorkSpace .

UserVolumeSizeGib -> (integer)

The size of the user storage. For important information about how to modify the size of the root and user volumes, see Modify a WorkSpace .

ComputeTypeName -> (string)

The compute type. For more information, see Amazon WorkSpaces Bundles .


Tags -> (list)

The tags for the WorkSpace.
(structure)

Describes a tag.
Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workspaces", "create-workspaces", "workspaces", add_option_dict)





