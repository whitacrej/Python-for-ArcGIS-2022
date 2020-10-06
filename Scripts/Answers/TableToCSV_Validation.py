import arcpy
class ToolValidator(object):
    """Class for validating a tool's parameter values and controlling
    the behavior of the tool's dialog."""

    def __init__(self):
        """Setup arcpy and the list of tool parameters."""
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        """Refine the properties of a tool's parameters.
        This method is called when the tool is opened."""
        # Disable the optional alias parameter
        self.params[3].enabled = False

    def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed."""

        if self.params[0].value and not self.params[0].hasBeenValidated:
            try:
                # Create a describe object for 'Input Table'
                desc = arcpy.Describe(self.params[0].value)

                # Check if 'Input Table' contains aliases, and if so enable Add Field Aliases to CSV Table (optional)' parameter
                aliases = [field.aliasName for field in desc.fields if field.aliasName != field.name]
                if aliases:
                    self.params[3].enabled = True
                else:
                    self.params[3].enabled = False

            except:
                pass
        return

    def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True
