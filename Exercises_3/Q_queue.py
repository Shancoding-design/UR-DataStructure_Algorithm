from collections import deque

# At RRA, 6 citizens queue.
# Initialize the queue
RRA_queue = deque()
# Citizens arrive
print("Citizens arriving at RRA:")
def RRA_arrive(citizen):
    RRA_queue.append(citizen)
    print(f"{citizen} has arrived.")
    return f"Current queue at RRA: {list(RRA_queue)}"
# Example arrivals
RRA_arrive("Citizen1")
RRA_arrive("Citizen2")
RRA_arrive("Citizen3")
RRA_arrive("Citizen4")
RRA_arrive("Citizen5")
RRA_arrive("Citizen6")
print(f"Queue after arrivals at RRA: {list(RRA_queue)} \n")

# After 2 served, who is next?
print(" After Serving 2 citizens at RRA, which are:")
def RRA_serve_two():
    for _ in range(2):
        if RRA_queue:
            served_citizen = RRA_queue.popleft()
            print(f"Served citizens {served_citizen}.")
        else:
            print("No more citizens to serve.")
            break
    return f"Current queue at RRA: {list(RRA_queue)}"
RRA_serve_two()
print(f"Queue after serving 2 citizens at RRA, it remains: {list(RRA_queue)} \n")

# At BK ATM, 7 clients queue.
# Initialize the queue
BK_ATM_client = deque()
print("Clients arriving at BK ATM:")
def BK_ATM_arrive(client):
    BK_ATM_client.append(client)
    print(f"{client} has arrived.")
    return f"Current queue at BK ATM: {list(BK_ATM_client)}"

# Example arrivals
BK_ATM_arrive("Client1")
BK_ATM_arrive("Client2")
BK_ATM_arrive("Client3")
BK_ATM_arrive("Client4")
BK_ATM_arrive("Client5")
BK_ATM_arrive("Client6")
BK_ATM_arrive("Client7")
print(f"Queue after arrivals at BK ATM: {list(BK_ATM_client)} \n")

# Who is served last?
print("Who is the last client served at BK ATM?")
def BK_ATM_serve_last():
    # Serve clients until only one remains
    while len(BK_ATM_client) > 1:
        served_client = BK_ATM_client.popleft()
        print(f"Served client is {served_client}.")
    # The last client remaining
    if BK_ATM_client:
        last_client = BK_ATM_client[0]
        print(f"The last client at BK ATM is: {last_client}")
    return f"Current queue at BK ATM: {list(BK_ATM_client)}"
BK_ATM_serve_last()
print(f"The last client at BK ATM, it remains: {list(BK_ATM_client)} \n")

# ueue vs stack for distributing IDs.
print("Queue vs Stack for distributing IDs:")
def distribute_IDs_queue(num_IDs):
    ID_queue = deque()
    for i in range(1, num_IDs + 1):
        ID_queue.append(f"ID{i}")
    distributed_IDs = []
    while ID_queue:
        distributed_IDs.append(ID_queue.popleft())
    return distributed_IDs
distributed_IDs = distribute_IDs_queue(5)
print(f"Distributed IDs using Queue: {distributed_IDs} \n")

# Stack vs Queue for distributing IDs.
def distribute_IDs_stack(num_IDs):
    ID_stack = []
    for i in range(1, num_IDs + 1):
        ID_stack.append(f"ID{i}")
    distributed_IDs = []
    while ID_stack:
        distributed_IDs.append(ID_stack.pop())
    return distributed_IDs
distributed_IDs_stack = distribute_IDs_stack(5)
print(f"Distributed IDs using Stack: {distributed_IDs_stack} \n")
 







