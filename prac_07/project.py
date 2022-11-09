class Project:
    def __init__(self, name, start_date, priority, cost, percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __str__(self):
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost}\t{self.percentage}"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.percentage == 100
