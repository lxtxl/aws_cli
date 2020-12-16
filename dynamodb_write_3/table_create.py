#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-table.html
if __name__ == '__main__':
    """
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-table.html
	describe-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-table.html
	list-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-tables.html
	update-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-table.html
    """

    parameter_display_string = """
    # attribute-definitions : An array of attributes that describe the key schema for the table and indexes.
(structure)

Represents an attribute for describing the key schema for the table and indexes.
AttributeName -> (string)

A name for the attribute.

AttributeType -> (string)

The data type for the attribute, where:

S - the attribute is of type String
N - the attribute is of type Number
B - the attribute is of type Binary
    # table-name : The name of the table to create.
    # key-schema : Specifies the attributes that make up the primary key for a table or an index. The attributes in KeySchema must also be defined in the AttributeDefinitions array. For more information, see Data Model in the Amazon DynamoDB Developer Guide .
Each KeySchemaElement in the array is composed of:

AttributeName - The name of this key attribute.
KeyType - The role that the key attribute will assume:

HASH - partition key
RANGE - sort key




Note
The partition key of an item is also known as its hash attribute . The term âhash attributeâ derives from the DynamoDB usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term ârange attributeâ derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

For a simple primary key (partition key), you must provide exactly one element with a KeyType of HASH .
For a composite primary key (partition key and sort key), you must provide exactly two elements, in this order: The first element must have a KeyType of HASH , and the second element must have a KeyType of RANGE .
For more information, see Working with Tables in the Amazon DynamoDB Developer Guide .
(structure)

Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.
AttributeName -> (string)

The name of a key attribute.

KeyType -> (string)

The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term âhash attributeâ derives from DynamoDBâs usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term ârange attributeâ derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("dynamodb", "create-table", "attribute-definitions", "table-name", "key-schema", add_option_dict)
