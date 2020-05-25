from classes.states import InitialState,GoalState
class Concrete_Planning:
    def __init__(self):
        self.concrete_planning = []
        self.size = 0
        self.required = False
        self.isAble = False
        self.id = "" # can be I_S , S_S, S_G
        self.abtract_step = -1
    def getSize(self):
        return self.size     
    def isRequire(self):
        return self.required
    
class Abtract_Planning: 
    def __init__(self):
        self.abtract_planning = []
        self.initial_state = InitialState()
        self.goal_state = GoalState()
        self.size = 0
    def __str__(self):
        return "Print"
    def __repr__(self):
        return "Print"
    def print_detail(self):
        print("--Intial---")
        print(self.initial_state.print_data_detail());
        print("--Goal---")
        print(self.goal_state.print_data_detail());
        print("--Sequence of abtract service class: ")
        for service in self.abtract_planning:
            print(service)
        print("--Size of sequence : ")
        print(self.size)
    def print_workflow(self,type):
        print("--Intial---")
        print(self.initial_state.print_data_detail());
        print("--Goal---")
        print(self.goal_state.print_data_detail());
        print("--Abtract Plan(s) : ")
        print("--------------------------------------------------------")
        step = 1
        if (type == "simple"):
            for service in self.abtract_planning:
                print("%s : %s" %(str(step), service.print_simple()))
                step = step + 1
        elif (type == "with_match_data"):
            for service in self.abtract_planning:
                print("%s : %s" %(str(step), service.print_with_match()))
                step = step + 1
        else:
            for service in self.abtract_planning:
                print("%s : %s" %(str(step), service.print_simple()))
                step = step + 1
        print("--------------------------------------------------------")
        print("--Size of sequence : %s" %(str(self.size)))

    def update_preprocessing_service(self):
        for service_class in self.abtract_planning:
            for match_data in service_class.remember_inputs_from_step:
                for check_service in self.abtract_planning:
                    if (match_data.existed_o_step == 0):
                        match_data.preprocessing_service_class = "initial_state"
                    else:    
                        if (match_data.existed_o_step == check_service.service_class_step + 1):
                            match_data.preprocessing_service_class =  check_service.service_class_name
                            break
                        
    def getSequecesOfAction(seft):
        return seft.abtract_planning
    def getSize(self):
        return self.size
    def addServiceClass(self, serivce):
        self.abtract_planning.append(serivce)
        self.size = self.size + 1
    def reorderSevices(self):
        self.abtract_planning.sort(key=lambda service: service.service_class_step, reverse=False)
    def getServiceClassFromWorkFlowByName(self, service_class_name):
        for service_class in self.abtract_planning:
            if (service_class.service_class_name.strip().upper() == service_class_name.strip().upper()):
                return service_class
        return None
    def getConcreteOperationFromWorkflowByNames(self, class_name, operation_name):
        for service_class in self.abtract_planning:
            if (service_class.service_class_name.strip().upper() == class_name.strip().upper()):
                for operation in service_class.service_operation_instances:
                    if (operation.service_instance_name.strip().upper() == operation_name.strip().upper()):
                        return operation
        return None