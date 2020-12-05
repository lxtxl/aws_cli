#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/batch-put-document.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # index-id : The identifier of the index to add the documents to. You need to create the index first using the  CreateIndex operation.
    # documents : One or more documents to add to the index.
Documents have the following file size limits.

5 MB total size for inline documents
50 MB total size for files from an S3 bucket
5 MB extracted text for any file

For more information about file size and transaction per second quotas, see Quotas .
(structure)

A document in an index.
Id -> (string)

A unique identifier of the document in the index.

Title -> (string)

The title of the document.

Blob -> (blob)

The contents of the document.
Documents passed to the Blob parameter must be base64 encoded. Your code might not need to encode the document file bytes if youâre using an AWS SDK to call Amazon Kendra operations. If you are calling the Amazon Kendra endpoint directly using REST, you must base64 encode the contents before sending.

S3Path -> (structure)

Information required to find a specific file in an Amazon S3 bucket.
Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.


Attributes -> (list)

Custom attributes to apply to the document. Use the custom attributes to provide additional information for searching, to provide facets for refining searches, and to provide additional information in the query response.
(structure)

A custom attribute value assigned to a document.
Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.
StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings.
(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.




AccessControlList -> (list)

Information to use for user context filtering.
(structure)

Provides user and group information for document access filtering.
Name -> (string)

The name of the user or group.

Type -> (string)

The type of principal.

Access -> (string)

Whether to allow or deny access to the principal.



ContentType -> (string)

The file type of the document in the Blob field.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kendra", "batch-put-document", "index-id", "documents", add_option_dict)
