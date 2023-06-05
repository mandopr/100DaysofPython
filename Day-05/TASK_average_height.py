# taking student height as string numbers seperated by spaces and then converted to list by split()
student_height = input("\nInput a list of student height by seperating with space : ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(f"\nAverage student height : {sum(student_height)/len(student_height)}")