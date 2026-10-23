import numpy as np
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])


print("Shape:", marks.shape)


print("Student averages:", np.round(np.mean(marks, axis=1), 2))



print("Subject averages:", np.round(np.mean(marks, axis=0), 2))


grace_marks = marks + 5


weights = np.array([0.3, 0.3, 0.4])
weighted_scores = marks @ weights


print("Weighted scores:", np.round(weighted_scores, 2))