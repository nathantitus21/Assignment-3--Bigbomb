import random

result_log = []

print("Welcome to the Elementary Bomb Lab!")
name = input("Enter your full name: ").strip()
result_log.append(f"Student Name: {name}")
random.seed(name)

def log_and_exit(phase_num, input_val):
    result_log.append(f"Phase {phase_num} Input: {input_val}")
    result_log.append(f"Phase {phase_num}: BOOM!")
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(result_log))
        f.write(f"\nExploded at Phase {phase_num}")
    print("BOOM! Wrong answer.")
    exit()

# -------- Phase 1 --------
print("\nPhase 1")
target = random.randint(15, 30)
print("Enter x such that x + 2 = {}".format(target))
x = int(input("Your answer: "))
if x + 2 != target:
    log_and_exit(1, x)
result_log.append(f"Phase 1 Input: {x}")
result_log.append("Phase 1: Defused")

# -------- Phase 2 --------
print("\nPhase 2")
secret = random.randint(5, 10)
print("Enter a number equal to the secret value.")
y = int(input("Your answer: "))
if y != secret:
    log_and_exit(2, y)
result_log.append(f"Phase 2 Input: {y}")
result_log.append("Phase 2: Defused")

# -------- Phase 3 --------
print("\nPhase 3")
start = random.randint(1, 3)
end = start + random.randint(3, 5)
expected = sum(range(start, end + 1))
print(f"Enter the sum from {start} to {end}.")
z = int(input("Your answer: "))
if z != expected:
    log_and_exit(3, z)
result_log.append(f"Phase 3 Input: {z}")
result_log.append("Phase 3: Defused")

# -------- Phase 4 --------
print("\nPhase 4")
target_count = random.randint(4, 6)
step = random.randint(1, 3)
print(f"Enter x such that loop: i=0; while i<x; i+= {step} runs exactly {target_count} times.")
x = int(input("Your answer: "))
i = 0
count = 0
while i < x:
    count += 1
    i += step
if count != target_count:
    log_and_exit(4, x)
result_log.append(f"Phase 4 Input: {x}")
result_log.append("Phase 4: Defused")

# -------- Phase 5: Nested Ifs --------
print("\nPhase 5")
a = random.randint(1, 10)
b = random.randint(1, 10)
if a>b:
    a,b= b,a
print(f"Given a = {a}, b = {b}. Enter x such that:")
print("  if x < a: boom")
print("  else if x < b: defused")
print("  else: boom")
x = int(input("Your answer: "))
if x < a or x >= b:
    log_and_exit(5, x)
result_log.append(f"Phase 5 Input: {x}")
result_log.append("Phase 5: Defused")

# -------- Phase 6: Nested If-Else Tree --------
print("\nPhase 6")
m = random.randint(10, 20)
print(f"Enter x such that:")
print("  if x < m:")
print("     if x % 2 == 0: defused")
print("     else: boom")
print("  else: boom")
x = int(input("Your answer: "))
if not (x < m and x % 2 == 0):
    log_and_exit(6, x)
result_log.append(f"Phase 6 Input: {x}")
result_log.append("Phase 6: Defused")

# -------- Phase 7: Multi-Branch Nesting --------
print("\nPhase 7")
k = random.randint(3, 6)
print(f"Enter x such that:")
print("  if x < k: boom")
print("  elif x == k: defused")
print("  elif x > k and x < k+3: boom")
print("  else: boom")
x = int(input("Your answer: "))
if x != k:
    log_and_exit(7, x)
result_log.append(f"Phase 7 Input: {x}")
result_log.append("Phase 7: Defused")

# -------- Phase 8: Nested Loop --------
print("\nPhase 8")
outer = random.randint(2, 4)
inner = random.randint(3, 5)
expected = outer * inner
print(f"How many times does this loop run?")
print(f"for i in range({outer}):")
print(f"   for j in range({inner}):")
print("       count += 1")
x = int(input("Your answer: "))
if x != expected:
    log_and_exit(8, x)
result_log.append(f"Phase 8 Input: {x}")
result_log.append("Phase 8: Defused")

# -------- Phase 9: Loop Iteration Count --------
print("\nPhase 9")
a = random.randint(5, 10)
print(f"How many iterations does this loop run?")
print(f"for i in range(0, {a}, 2):")
print("    count += 1")
count = 0
for i in range(0, a, 2):
    count += 1
x = int(input("Your answer: "))
if x != count:
    log_and_exit(9, x)
result_log.append(f"Phase 9 Input: {x}")
result_log.append("Phase 9: Defused")

# -------- Phase 10: Zero-Iteration Loop --------
print("\nPhase 10")
low = random.randint(5, 10)
print(f"How many times does this loop run?")
print(f"for i in range({low}, 3):")
print("    count += 1")
x = int(input("Your answer: "))
if x != 0:
    log_and_exit(10, x)
result_log.append(f"Phase 10 Input: {x}")
result_log.append("Phase 10: Defused")

# -------- Final Success --------
print(f"\nCongratulations, {name}! Bomb fully defused.")
result_log.append("Bomb fully defused")
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(result_log))

