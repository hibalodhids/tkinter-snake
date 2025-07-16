import numpy as np

scores = np.array([
    [88, 92, 79, 93],
    [76, 85, 83, 80],
    [90, 91, 87, 89],
    [98, 70, 60, 72],
    [95, 90, 94, 90]
])

student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Hiba']
subject_names = ['Math', 'Science', 'English', 'History']


# Average score per student
average_scores = np.mean(scores, axis=1)
# Average score per subject
avg_per_subject = np.mean(scores, axis=0)
# Highest and lowest scoring student
best_student_idx = np.argmax(average_scores)
worst_student_idx = np.argmin(average_scores)
# Highest and lowest scoring subject

best_subject_idx = np.argmax(avg_per_subject)
worst_subject_idx = np.argmin(avg_per_subject)

# Results
print("Average score per student:")
#
# for i ,avg_per_subject in enumerate(average_scores):
#     print(student_names[best_student_idx], avg_per_subject)

for i, avg in enumerate(average_scores):
    print(f"{student_names[i]}: {avg:.2f}")

for i, avg in enumerate(avg_per_subject):
    print(f"{subject_names[i]}: {avg:.2f}")

print(f"\nTop student: {student_names[best_student_idx]} with average score {average_scores[best_student_idx]:.2f}")
print(f"Lowest scoring student: {student_names[worst_student_idx]} with average score {average_scores[worst_student_idx]:.2f}")

print(f"\nBest subject: {subject_names[best_subject_idx]} with average score {avg_per_subject[best_subject_idx]:.2f}")
print(f"Worst subject: {subject_names[worst_subject_idx]} with average score {avg_per_subject[worst_subject_idx]:.2f}")



