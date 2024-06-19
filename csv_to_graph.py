# source /bin/activate

import csv
import matplotlib
import matplotlib.pyplot

def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

with open("./Anwesenheiten - Tabellenblatt1.csv", newline="") as csv_file:
    data_reader = csv.reader(csv_file, delimiter=",")

    x_values = []
    y_values = []
    errors = []
    x_indices = {}

    # Skip the first row (header)
    x_head, y_head = (next(data_reader))

    for i, row in enumerate(data_reader):
        if row[0] == "" or row[1] == "":
            continue
        
        x_indices[row[0]] = i

        if is_number(row[1]):
            x_values.append(row[0])
            y_values.append(int(row[1]))
        else:
            errors.append((row[0], row[1]))
            x_values.append(row[0])
            y_values.append(0)

matplotlib.pyplot.figure(figsize=(15, 5))

matplotlib.pyplot.plot(x_values, y_values, marker="o", linestyle="-", color="blue", label="Anwesenheiten")
matplotlib.pyplot.xlabel(x_head, fontsize=14)
matplotlib.pyplot.ylabel(y_head, fontsize=14)

matplotlib.pyplot.title('AlgDat Tutorium SOSE 2024 Anwesenheiten', fontsize=16)
matplotlib.pyplot.xticks(rotation=45, fontsize=12, ha="right")  # Rotate x-axis labels for better readability
matplotlib.pyplot.yticks(fontsize=12)

# Add Errors
for x, error in errors:
    # print(f"Error: {error} at {x}")
    # print(f"DEBUG {x_values.index(x)}")
    x_position = x_values.index(x)
    matplotlib.pyplot.annotate(error, (x_position, y_values[x_position] if x_position < len(y_values) else 0), textcoords="offset points", xytext=(0, 10), ha="center")

matplotlib.pyplot.xticks(rotation=45)  # Rotate labels to 45 degrees
matplotlib.pyplot.grid()
matplotlib.pyplot.tight_layout()  # Adjust layout to make room for the rotated labels
matplotlib.pyplot.show()