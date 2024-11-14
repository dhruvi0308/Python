def threshold(students_scores, threshold):
    names_above_threshold = []

    for name, score in students_scores:
        if score >= threshold:
            names_above_threshold.append(name)

    return names_above_threshold

students_scores = [("Alice", 85), ("Bob", 70), ("Charlie", 95), ("David", 65)]
threshold = 75
result = threshold(students_scores, threshold)
print(result)
