import mlflow

# step-1
def calculator(a,b):
    return (a+b)

if __name__ == "__main__":
    a,b = 2394, 1290
    result=calculator(a,b)
    print(f"my result is {result}")

# Step-2
def calculator(a,b,operation=None):
    if operation == 'add':
        return (a+b)
    if operation == 'sub':
        return (a-b)
    if operation == 'mul':
        return (a*b)
    if operation == 'div':
        return (a/b)

if __name__ == "__main__":
    a,b,operation = 1, 0, 'div'
    result=calculator(a,b,operation)
    print(f"my result is {result}")

# Step-3 with mlflow
def calculator(a,b,operation=None):
    if operation == 'add':
        return (a+b)
    if operation == 'sub':
        return (a-b)
    if operation == 'mul':
        return (a*b)
    if operation == 'div':
        return (a/b)

if __name__ == "__main__":
    a,b,operation = 1995, 2024, 'div'
    with mlflow.start_run():
        result=calculator(a,b,operation)
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param("operation",operation)
        print(f"my result regarding {operation} is {result}")
        mlflow.log_param("result",result)

