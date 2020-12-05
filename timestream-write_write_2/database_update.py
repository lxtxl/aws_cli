#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/update-database.html
if __name__ == '__main__':
    """
	create-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-database.html
	delete-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/delete-database.html
	describe-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/describe-database.html
	list-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/list-databases.html
    """

    parameter_display_string = """
    # database-name : The name of the database.
    # kms-key-id : The identifier of the new KMS key (KmsKeyId ) to be used to encrypt the data stored in the database. If the KmsKeyId currently registered with the database is the same as the KmsKeyId in the request, there will not be any update.
You can specify the KmsKeyId using any of the following:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
Alias name: alias/ExampleAlias
Alias ARN: arn:aws:kms:us-east-1:111122223333:alias/ExampleAlias
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("timestream-write", "update-database", "database-name", "kms-key-id", add_option_dict)
