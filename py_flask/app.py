from flask import Flask, request, jsonify

app = Flask(__name__)

def max_risk_mitigated(inputs):
    results = []
    for input_data in inputs:
        n, m = map(int, input_data[0].split())
        costs = list(map(int, input_data[1].split()))

        max_risk = 0
        for i in range(m):
            for j in range(i + 1, m):
                risk_mitigated = costs[j] - costs[i]
                if risk_mitigated > 0:
                    max_risk = max(max_risk, risk_mitigated)

        results.append(max_risk)

    return {"answer": results}

@app.route('/risk-mitigation', methods=['POST'])
def risk_mitigation():
    try:
        data = request.json['inputs']
        result = max_risk_mitigated(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
