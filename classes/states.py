class CommonAsset_DataFormat:
    def __init__(self,resource_name,data_format):
        self.resource_name = resource_name
        self.resource_data_format = data_format
    
    def __str__(self):
        return "(%s,%s)" %(self.resource_name,self.resource_data_format)

    def print_data_detail(self):
        return "(%s,%s)" %(self.resource_name,self.resource_data_format)

class InitialState:
    def __init__(self):
        self.fact = "initially"
        self.assets = [] # CommonAsset_DataFormat list
    def print_data_detail(self):
        assets_data = ""
        for asset in self.assets:
            assets_data += " " + asset.print_data_detail()
        return '{%s}' %(assets_data)
class GoalState:
    def __init__(self):
        self.fact = "finally"
        self.assets = [] # CommonAsset_DataFormat list
    def print_data_detail(self):
        assets_data = ""
        for asset in self.assets:
            assets_data += " " + asset.print_data_detail()

        return "{%s}" % (assets_data)