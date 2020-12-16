#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html
if __name__ == '__main__':
    """
	describe-restore-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-restore-job.html
	list-restore-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-jobs.html
    """

    parameter_display_string = """
    # recovery-point-arn : An ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .
    # metadata : A set of metadata key-value pairs. Contains information, such as a resource name, required to restore a recovery point.
You can get configuration metadata about a resource at the time it was backed up by calling GetRecoveryPointRestoreMetadata . However, values in addition to those provided by GetRecoveryPointRestoreMetadata might be required to restore a resource. For example, you might need to provide a new resource name if the original already exists.
You need to specify specific metadata to restore an Amazon Elastic File System (Amazon EFS) instance:

file-system-id : The ID of the Amazon EFS file system that is backed up by AWS Backup. Returned in GetRecoveryPointRestoreMetadata .
Encrypted : A Boolean value that, if true, specifies that the file system is encrypted. If KmsKeyId is specified, Encrypted must be set to true .
KmsKeyId : Specifies the AWS KMS key that is used to encrypt the restored file system. You can specify a key from another AWS account provided that key it is properly shared with your account via AWS KMS.
PerformanceMode : Specifies the throughput mode of the file system.
CreationToken : A user-supplied value that ensures the uniqueness (idempotency) of the request.
newFileSystem : A Boolean value that, if true, specifies that the recovery point is restored to a new Amazon EFS file system.
ItemsToRestore : A serialized list of up to five strings where each string is a file path. Use ItemsToRestore to restore specific files or directories rather than the entire file system. This parameter is optional.

key -> (string)
value -> (string)
    # iam-role-arn : The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("backup", "start-restore-job", "recovery-point-arn", "metadata", "iam-role-arn", add_option_dict)
