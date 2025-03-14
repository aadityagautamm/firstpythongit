from enum import Enum

class Status(Enum):
    pending = 1
    processing = 2
    completed = 3
    failed = 4

def get_status (status):
    if status == Status. pending:
        return "Pending"
    elif status == Status.processing:
        return "Processing"
    elif status == Status.completed:
        return "Completed"
    else :
        return "Failed"

print (get_status(Status.pending))
print (get_status(Status.processing))
print (get_status(Status.completed))
print (get_status(Status.failed))