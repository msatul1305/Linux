from flask import Flask, request, jsonify

app = Flask(__name__)

def risk_mitigation(inputs):
    results = []
    for input_data in inputs:
        n, a = map(int, input_data[0].split())
        a_values = list(map(int, input_data[1].split()))
        results.append(calculate(n, a_values))
    return results

def calculate(strategies, input_values):
    n = len(input_values)
    max_diff_array = [0] * n

    for i in range(n - 1, 0, -1):
        max_diff = 0
        for j in range(i - 1, -1, -1):
            max_diff = max(max_diff, input_values[i] - input_values[j])
        max_diff_array[i] = max_diff

    max_diff_array.sort(reverse=True)

    result = sum(max_diff_array[:strategies])

    return result

@app.route('/risk-mitigation', methods=['POST'])
def risk_mitigation_endpoint():
    data = request.json
    inputs = data.get('inputs', [])
    results = risk_mitigation(inputs)

    return jsonify({"answer": results})

if __name__ == '__main__':
    app.run(debug=True)
