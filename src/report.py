

class Report():
    
    def __init__(self, save_report=False, file_path="reports/") -> None:
        self.report_metrics = {}
        self.save_report = save_report
        self.file_path = file_path

    def register_strategy(self, strategy):
        self.report_metrics["strategy"] = strategy
    
    def register_simulation_period(self, init_period, final_period):
        self.report_metrics["init_period"] = init_period
        self.report_metrics["final_period"] = final_period
        self.report_metrics["total_simulation_period"] = final_period-init_period
    
    def register_n_operations(self, total_op):
        self.report_metrics["n_operations"] = total_op
    
    def register_initial_budget(self, initial_budget):
        self.report_metrics["initial_budget"] = initial_budget
    
    def register_final_budget(self, final_budget):
        print(final_budget)
        self.report_metrics["final_budget"] = final_budget
    
    def register_taxes(self, fixed_comission, variable_comission, min_tax):
        self.report_metrics["fixed_comission"] = fixed_comission
        self.report_metrics["variable_comission"] = variable_comission
        self.report_metrics["min_tax"] = min_tax

    def register_total_comissions(self, total_comissions):
        self.report_metrics["total_comissions"] = total_comissions

    def compute_positions_metrics(self, position_list):
        # Porcentaje ops exito
        # Beneficio medio de ops exito
        # Perdida media de ops failed
        succes_counter = 0
        mean_profit = 0
        mean_loss = 0
        self.register_n_operations(len(position_list))
        for pos in position_list:
            result = (pos.close_price - pos.open_price)/pos.open_price
            if result >0:
                succes_counter +=1
                mean_profit += result
            else:
                mean_loss += result
        if succes_counter != 0:
            self.mean_profit = mean_profit / succes_counter
            self.success_rate = succes_counter / len(position_list)
        else:
            self.mean_profit =0
            self.success_rate = 0
        if (len(position_list)-succes_counter) != 0:
            self.mean_loss = mean_loss / (len(position_list)-succes_counter)
        else:
            self.mean_loss = 0
            
        


    def print_report(self):
        print(f"{'#'*20}")
        print("\n## Simulation ended")
        print("\n# Global statistics")
        print(f"Duration: {self.report_metrics['total_simulation_period']}")
        print(f"Number of operations: {self.report_metrics['n_operations']}")
        print(f"Fixed comission value: {self.report_metrics['variable_comission']}")
        print(f"Variable comission value: {self.report_metrics['fixed_comission']}")
        print(f"Min comission value: {self.report_metrics['min_tax']}")
        print(f"Initial budget: {self.report_metrics['initial_budget']}")
        print(f"Final budget: {self.report_metrics['final_budget']}")
        a = self.report_metrics['final_budget'] / self.report_metrics['initial_budget']
        print(f"Performance: {a}")
        print(f"Total comissions: {self.report_metrics['total_comissions']}")
        print(f" Ratio comissions/final_budget: {100*self.report_metrics['total_comissions']/self.report_metrics['final_budget']}%")

        print("\n# Strategy")
        print(f"Strategy: {self.report_metrics['strategy'].get_name()}")
        print(f"Strategy parameters:")
        for key in self.report_metrics['strategy'].__dict__.keys():
            print(f"  - {key}: {self.report_metrics['strategy'].__dict__[key]}")
        # print(f"Strategy parameters {self.report_metrics['strategy'].__dict__}")

        print("\n# Strategy results")
        print(f"Number of operations: {self.report_metrics['n_operations']}")
        print(f"Success Rate: {self.success_rate*100}%")
        print(f"Mean profits in SUCCESSFUL operations: {self.mean_profit*100}%")
        print(f"Mean losses in FAILED operations: {self.mean_loss*100}%")


        # if self.save_report==True:
        #     self.save_report_file()

    def save_report_file(self):
        report = ""
        report += f"{'#'*20}\n"
        report += f"Duration: {self.report_metrics['total_simulation_period']}\n"
        report += f"Initial budget: {self.report_metrics['initial_budget']}\n"
        report += f"Number of operations: {self.report_metrics['n_operations']}\n"
        report += f"Final budget: {self.report_metrics['final_budget']}\n"
        print(self.report_metrics["strategy"].get_name())
        print(str(self.report_metrics['init_period']))
        report += f"Performance: {self.report_metrics['final_budget'] / self.report_metrics['initial_budget']}\n"
        filename_report = self.file_path+str(self.report_metrics["strategy"].get_name()) \
                            +"_"+str(self.report_metrics['init_period'])[0:9]+"_" \
                            + str(self.report_metrics['final_period'])[0:9]+".txt"
        print(filename_report)
        with open(filename_report,'x') as f:
            f.write(report)

