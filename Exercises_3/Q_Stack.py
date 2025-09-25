# UR pushes ["QuizA", "QuizB", "QuizC"]. in stack
# declare array store UR quiz
Ur_stack = []

print("Pushing QuizA, QuizB, QuizC onto the stack. \n")
def UR_push(quiz):
    Ur_stack.append(quiz)
    print(f"Pushed {quiz} onto the stack.")
    return f"Current stack: {Ur_stack}"

# example pushes 3 quizzes
UR_push("QuizA") 
UR_push("QuizB")
UR_push("QuizC")
print(f"Stack after pushes: {Ur_stack} \n")

# UR undo one quiz
print("Undoing the last quiz (popping from stack). \n")
def UR_pop():
    if Ur_stack:
        removed_quiz = Ur_stack.pop()
        print(f"Undo {removed_quiz} from the stack.")
    else:
        print("No quizzes to remove.")
    return f"Current stack: {Ur_stack}"

UR_pop()
print(f"Stack after one undo: {Ur_stack} \n")

# UR quiz on the top of the stack
print("Viewing the top quiz on the stack without removing it. \n")
def UR_view_top():
    if Ur_stack:
        top_quiz = Ur_stack[-1]
        print(f"Top quiz on the stack is: {top_quiz}")
    else:
        print("The stack is empty.")
    return f"Current stack: {Ur_stack}"

UR_view_top()

# In Irembo, push ["StepA", "StepB", "StepC"] onto the stack
# declare array store Irembo steps
Irembo_stack = []
print("\nPushing StepA, StepB, StepC onto the stack. \n")
def Irembo_push(step):
    Irembo_stack.append(step)
    print(f"Pushed {step} onto the stack of Irembo.")
    return f"Current stack in Irembo: {Irembo_stack}"
# example pushes 3 steps
Irembo_push("StepA")
Irembo_push("StepB")
Irembo_push("StepC")
print(f"Stack after pushes in Irembo: {Irembo_stack} \n")

# POP all in stack of irembo
print("Popping all steps from the Irembo stack. \n")
def Irembo_pop_all():
    while Irembo_stack:
        removed_step = Irembo_stack.pop()
        print(f"Popped {removed_step} from the Irembo stack.")
    return f"Current stack in Irembo: {Irembo_stack}"
Irembo_pop_all()
print(f"Stack after popping all in Irembo: {Irembo_stack} \n")
print (f"Final irembo stack remains are: {Irembo_stack} \n")

# challanges push ["1","2","3"] onto the stack
# declare array store challanges
challanges_stack = []
print("Pushing 1, 2, 3 onto the challanges stack. \n")
def challanges_push(item):
    challanges_stack.append(item)
    print(f"Pushed {item} onto the challanges stack.")
    return f"Current challanges stack: {challanges_stack}"
# example pushes 3 items
challanges_push("1")
challanges_push("2")
challanges_push("3")
print(f"Challanges stack after pushes: {challanges_stack} \n")

# challanges pop two items
print("Popping two items from the challanges stack. \n")
def challanges_pop_two():
    for _ in range(2):
        if challanges_stack:
            removed_item = challanges_stack.pop()
            print(f"Popped {removed_item} from the challanges stack.")
        else:
            print("No more items to pop from the challanges stack.")
            break
    return f"Current challanges stack: {challanges_stack}"
challanges_pop_two()
print(f"Challanges stack after popping two items: {challanges_stack} \n")

# pushes 4
print("Pushing 4 onto the challanges stack. \n")
challanges_push("4")
print(f"Challanges stack after pushing 4: {challanges_stack} \n")

# view top of challanges stack
print("Viewing the top item on the challanges stack without removing it. \n")
def challanges_view_top():
    if challanges_stack:
        top_item = challanges_stack[-1]
        print(f"Top item on the challanges stack is: {top_item}")
    else:
        print("The challanges stack is empty.")
    return f"Current challanges stack: {challanges_stack}"
challanges_view_top()
