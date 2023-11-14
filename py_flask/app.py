from flask import Flask, request, jsonify

app = Flask(__name__)

def get_time_intervals(inputs):
    result = []

    for input_set in inputs:
        n, *employee_names_and_shifts = input_set
        n = int(n)

        shifts = [(int(employee_names_and_shifts[i]), int(employee_names_and_shifts[i + 1]), employee_names_and_shifts[i + 2]) for i in range(0, len(employee_names_and_shifts), 3)]

        time_intervals = set()
        for _, end_time, _ in shifts:
            time_intervals.add(_)
            time_intervals.add(end_time)

        time_intervals = sorted(list(time_intervals))

        output_intervals = []
        for i in range(len(time_intervals) - 1):
            start_time, end_time = time_intervals[i], time_intervals[i + 1]
            employees_at_desk = []

            for employee_name, shift_start, shift_end in shifts:
                if shift_start <= start_time < shift_end or shift_start < end_time <= shift_end:
                    employees_at_desk.append(employee_name)

            employees_at_desk.sort()
            output_intervals.append((start_time, end_time, len(employees_at_desk), " ".join(employees_at_desk)))

        result.append([len(output_intervals)] + output_intervals)

    return {"answer": result}

@app.route('/time-intervals', methods=['POST'])
def time_intervals():
    try:
        data = request.json
        inputs = data["inputs"]
        response = get_time_intervals(inputs)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
