import random
from questions import QUESTIONS
q, a = random.choice(QUESTIONS)
print("Quick Quiz:")
ans = input(q + " ").strip()
print(" Correct!" if ans.lower() == a.lower() else f" Wrong — answer is: {a}")
