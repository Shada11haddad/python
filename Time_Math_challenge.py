import random
import time
OPERATOR = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
Total_Problems = 10 

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATOR)

    expr = str(left)+" "+operator +" "+str(right)
    print(expr)
    answer = eval(expr)

    return expr,answer
worng = 0
input("Press enter to start!")
print("-----------------")

start_time = time.time()
for i in range(Total_Problems):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1)+": "+ expr + "=")
        if guess == str(answer):
            break
        worng +=1
end_time = time.time()
total_time = end_time - start_time


print("-----------------")
print("Nice work! You finished in", total_time , " seconds!")
