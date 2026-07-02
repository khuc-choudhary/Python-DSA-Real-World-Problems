# H2) Toll Plaza Simulation (Circular Queue)
# A toll plaza has a fixed capacity of 5 vehicles.
# If full, new vehicles must wait.
# Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.
size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(vehicle):
    global front, rear

    if (rear + 1) % size == front:
        print("Toll Plaza is Full")
        return

    if front == -1:
        front = rear = 0
    else:
        rear = (rear + 1) % size

    queue[rear] = vehicle
    print(vehicle, "entered")

def dequeue():
    global front, rear
    if front == -1:
        print("Toll Plaza is Empty")
        return

    print(queue[front], "left")
    queue[front] = None

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size

def display():
    if front == -1:
        print("Empty")
        return

    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

enqueue("Car")
enqueue("Bus")
enqueue("Truck")
enqueue("Bike")
enqueue("Van")

display()

dequeue()
dequeue()

enqueue("Taxi")
enqueue("Auto")

display()