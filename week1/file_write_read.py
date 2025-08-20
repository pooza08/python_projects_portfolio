with open("tasks.txt", "w") as f:
    f.write("tasks completed. \n")
with open("tasks.txt", "a") as f:
    f.write("verified. \n")
with open("tasks.txt", "r") as f:
   content = f.read()
   print("file content. \n", content)
