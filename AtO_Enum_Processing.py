# =============== IMPORTS ================
import json
import re


# =============== CONSTANTS ================
ASSETS_RIPPED_PATH = "/mnt/e/Coding/Decompilation/AtO Decompiled"
ENUMS_PATH = ASSETS_RIPPED_PATH + "/Enums.cs"

JSON_OUTPUT_PATH = "/mnt/e/Coding/Decompilation/AtO Processing Output/enums.json"
PYTHON_OUTPUT_PATH = "/mnt/e/Coding/Decompilation/AtO-Processing/CSharpToPythonConversions/Enums.py"

ENUM_PREFIX = "public enum "
ENUM_PREFIX_LEN = len(ENUM_PREFIX)

ENUM_VALUE_PREFIX = "\r\n\t\t"
ENUM_VALUE_PREFIX_LEN = len(ENUM_VALUE_PREFIX)


# =============== VARIABLES ================
enums = {}
enumsHumanized = {}


# =============== READING ENUMS FILE ================
print ("Reading the enums file from " + ENUMS_PATH)
enumsFile = open(ENUMS_PATH, "r")
enumsFileTxt = enumsFile.read()
enumsFile.close()
print ("\tDone reading\n")


# =============== PROCESSING ENUMS INTO JSON ================
enumPrefixIndices = [m.start() for m in re.finditer(ENUM_PREFIX, enumsFileTxt)]
#enumIndices = map(lambda i : i + ENUM_PREFIX_LEN, enumPrefixIndices)

print ("Iterating over each enum in the file")
for i in enumPrefixIndices:
    # Title
    titleIndex = i + ENUM_PREFIX_LEN
    titleEndIndex = enumsFileTxt.find("\r\n", i)
    title = enumsFileTxt[titleIndex:titleEndIndex]

    # Values
    valuesIndex = enumsFileTxt.find("{", i)
    valuesEndIndex = enumsFileTxt.find("}", i)
    
    valuesSubstring = enumsFileTxt[valuesIndex:valuesEndIndex]
    valuesIndices = [m.start() for m in re.finditer(ENUM_VALUE_PREFIX, valuesSubstring)]

    values = []
    for vi in valuesIndices:
        valueIndex = vi + ENUM_VALUE_PREFIX_LEN
        valueEndIndex = valuesSubstring.find(",", valueIndex, valuesEndIndex)
        if (valueEndIndex < 0):
            valueEndIndex = valuesSubstring.find("\r\n", valueIndex)
        value = valuesSubstring[valueIndex:valueEndIndex]
        values.append(value)

    # Save to the enums dictionary
    enums[title] = values

print ("\tDone iterating. Processed " + str(len(enums)) + " enums\n")


# =============== HUMANIZE ENUM VALUES ================
# TODO


# =============== EXPORTING JSON ================
enumsJsonString = json.dumps(enums)

print ("Writing to " + JSON_OUTPUT_PATH)
file = open(JSON_OUTPUT_PATH, "w")
file.write(enumsJsonString)
file.close()
print ("\tDone writing\n")


# =============== CONVERT TO PYTHON & EXPORT ================
print ("Converting to Python")
pyStr = "class Enums(object):\n"
for enumKey in enums:
    i = 0
    pyStr += "\tclass " + enumKey + ":\n"
    for val in enums[enumKey]:
        if val == "None":
            val = "_None"
        pyStr += "\t\t" + val
        if "=" not in val:
            pyStr += " = " + str(i)
            i += 1
        pyStr += "\n"

print ("\tDone converting to Python\n")

print ("Writing to " + PYTHON_OUTPUT_PATH)
file = open(PYTHON_OUTPUT_PATH, "w")
file.write(pyStr)
file.close()
print ("\tDone writing\n")
