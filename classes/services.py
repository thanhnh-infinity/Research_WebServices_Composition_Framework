class Match_Object:
    def __init__(self,name,r_input,step,e_output,o_step):
        self.match_predicate = "match"
        self.service_class_name = name
        self.match_input = r_input
        self.match_step = step
        self.existed_o = e_output
        self.existed_o_step = o_step
        self.preprocessing_service_class = "UNKNOWN"
    def print_simple(self):
        return "(%s,%s,%d,%s,%d,%s)" %(self.service_class_name,self.match_input,self.match_step,self.existed_o,self.existed_o_step,self.preprocessing_service_class)
class Service_Class:
    def __init__(self,name,step):
        self.service_class_predicate = "occur"
        self.service_class_name = name
        self.service_class_step = step
        self.service_class_has_input = []
        self.service_class_has_output = []
        self.service_operation_instances = [] # Contain list of instance_services object
        self.remember_inputs_from_step = []
    def __str__(self):
        op_data = ""
        for operation in self.service_operation_instances:
            op_data += " " + operation.print_data_detail()

        return "(%s,%d,%s,%s,%s)" %(self.service_class_name,self.service_class_step,str(self.service_class_has_input),str(self.service_class_has_output),op_data)

    def print_simple(self):
        return "(%s,%d,%s,%s)" %(self.service_class_name,self.service_class_step,str(self.service_class_has_input),str(self.service_class_has_output))
    
    def print_with_match(self):
        data = "(%s,%d, INPUT%s, OUTPUT%s)" %(self.service_class_name,self.service_class_step,str(self.service_class_has_input),str(self.service_class_has_output))
        match_data = ""
        for match in self.remember_inputs_from_step:
            match_data += "\n %s".rjust(10) %(str(match.print_simple()))
        return "%s %s" %(str(data),str(match_data))

    def hasAnInstance(self, service_instance):
        if (service_instance.service_instance_of_class == self.service_class_name):
            for operation in self.service_operation_instances:
                if (service_instance.service_instance_name == operation.service_instance_name):
                    return True
            return False
        else:
            return False
    

class Service_Instance:
    def __init__(self,name,in_class,step):
        self.service_instance_predicate = "possible_concrete_operation"
        self.service_instance_name = name
        self.service_instance_of_class = in_class
        self.service_instance_abtract_step = step
        self.service_instance_concrete_step = 0
        self.service_instance_input_data_format = [] # Contain list of instances_data_format
        self.service_instance_output_data_format = [] # Contain list of instances_data_format
    
    def __str__(self):
        return "(%s,%s,%d)" %(self.service_instance_name,self.service_instance_of_class,self.service_instance_abtract_step)
    def getSignature(self):
        return "occur_concrete_operation(%s,%s,%d)" %(self.service_instance_name,self.service_instance_of_class,self.service_instance_abtract_step)
    def print_data_detail(self):
        in_format = ""
        out_format = ""
        for input_format in self.service_instance_input_data_format:
            in_format += input_format.print_data_detail()
        for output_format in self.service_instance_output_data_format:
            out_format += output_format.print_data_detail()

        return "(%s,%s,%d,%s,%s)" %(self.service_instance_name,self.service_instance_of_class,self.service_instance_abtract_step,str(in_format),str(out_format))    

class DataFormatObject:
    def __init__(self,op_instance_name,resource_name,data_format):
        self.op_instance_name = op_instance_name
        self.resource_name = resource_name
        self.resource_data_format = data_format
    
    def __str__(self):
        return "(%s,%s,%s)" %(self.op_instance_name,self.resource_name,self.resource_data_format)

    def print_data_detail(self):
        return "(%s,%s,%s)" %(self.op_instance_name,self.resource_name,self.resource_data_format)