#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/batch-write-item.html
if __name__ == '__main__':
    """
	transact-write-items : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/transact-write-items.html
    """

    parameter_display_string = """
    # request-items : A map of one or more table names and, for each table, a list of operations to be performed (DeleteRequest or PutRequest ). Each element in the map consists of the following:

DeleteRequest - Perform a DeleteItem operation on the specified item. The item to be deleted is identified by a Key subelement:

Key - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.


PutRequest - Perform a PutItem operation on the specified item. The item to be put is identified by an Item subelement:

Item - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values are rejected with a ValidationException exception. If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the tableâs attribute definition.



key -> (string)
value -> (list)

(structure)

Represents an operation to perform - either DeleteItem or PutItem . You can only request one of these operations, not both, in a single WriteRequest . If you do need to perform both of these operations, you need to provide two separate WriteRequest objects.
PutRequest -> (structure)

A request to perform a PutItem operation.
Item -> (map)

A map of attribute name to attribute values, representing the primary key of an item to be processed by PutItem . All of the tableâs primary key attributes must be specified, and their data types must match those of the tableâs key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true





DeleteRequest -> (structure)

A request to perform a DeleteItem operation.
Key -> (map)

A map of attribute name to attribute values, representing the primary key of the item to delete. All of the tableâs primary key attributes must be specified, and their data types must match those of the tableâs key schema.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dynamodb", "batch-write-item", "request-items", add_option_dict)





