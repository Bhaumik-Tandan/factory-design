"""
* Report Generator Factory:
* 		Build a ReportGeneratorFactory to create report generators (SalesReport, ExpenseReport) based on user requests.
"""

class ReportGeneratorFactory:
    def createReport(self, reportType):
        if reportType == "Sales":
            return SalesReport()
        elif reportType == "Expense":
            return ExpenseReport()
        else:
            return None

class SalesReport:
    def generateReport(self):
        print("Sales Report")

class ExpenseReport:
    def generateReport(self):
        print("Expense Report")

def main():
    factory = ReportGeneratorFactory()

    salesReport = factory.createReport("Sales")
    expenseReport = factory.createReport("Expense")

    reports = [salesReport, expenseReport]
    for report in reports:
        report.generateReport()

if __name__ == "__main__":
    main()