# -*- coding: UTF-8 -*-

''' Metadata, Copyright, License:
------------------------------------------------------------------------
Name:       TableToCSV.py
Purpose:    This script converts a table to a CSV table with selected
            fields.
Author:     Whitacre, James
Created:    2019/10/16
Copyright:  Copyright <Your Organization/Name> <YYYY>
Licence:    Licensed under the Apache License, Version 2.0 (the
            "License"); you may not use this file except in compliance
            with the License. You may obtain a copy of the License at
            http://www.apache.org/licenses/LICENSE-2.0
            Unless required by applicable law or agreed to in writing,
            software distributed under the License is distributed on an
            "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
            either express or implied. See the License for the specific
            language governing permissions and limitations under the
            License.
------------------------------------------------------------------------
'''

''' Import Modules '''
import arcpy
import csv


''' Parameters '''

# Input feature class or standalone table
input_table = arcpy.management.MakeFeatureLayer('https://services2.arcgis.com/eQgAMgHr2CRobt2r/arcgis/rest/services/UnconventionalWellsPA/FeatureServer/0', 'Unconventional Wells')

# Create user-defined list of the feature class or standalone table field names to be exported
field_names = ['Shape', 'PERMIT_NO', 'FARM_NAME', 'COUNTY', 'PROD_GAS_QUANT']

# Create a new output CSV file
# Replace the '...' with the location where you placed your downloaded data
# output_csv = r'C:\...\Advanced_PythonForArcGIS\ExerciseData\CSV\UnconventionalWells.csv'
output_csv = r'C:\Users\whitacrej\Documents\GitHub\Python-For-ArcGIS-2019\Advanced_PythonForArcGIS\ExerciseData\CSV\UnconventionalWells.csv'


''' Script '''

# Read the feature class or standalone table data

# Create an empty list to append data to
data = []

# Create a search cursor to access the data
with arcpy.da.SearchCursor(input_table, field_names) as cursor:
    for row in cursor:
        # Append each row to the data list
        data.append(row)


# Open the new output CSV file

# Python 2.x...For some reason, 'w' adds an extra line between rows, use 'wb' instead...
# with open(output_csv, 'wb') as csv_file:

# Python 3.x
with open(output_csv, 'w', newline='') as csv_file:
    # Creates CSV Writer object
    csv_writer = csv.writer(csv_file)
    
    # Write the field names to the new CSV file
    csv_writer.writerow(field_names)
    
    # Write the feature class or standalone table data to the new CSV file
    csv_writer.writerows(data)

# Message that the script is finished
print("CSV file complete; located at {}".format(output_csv))