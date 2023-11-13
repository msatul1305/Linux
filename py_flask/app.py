from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                          format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)


def longest_palindromic_arrangement(s):
    countr = {}
    for char in s:
        countr[char] = countr.get(char, 0) + 1
    len = 0
    is_odd = False
    for c in countr.values():
        len += c // 2 * 2
        if c % 2 == 1:
            is_odd = True
    if is_odd:
        len += 1
    return len


@app.route('/file-reorganization', methods=['POST'])
def file_reorganization():
    data = request.json
    inputs = data.get('inputs', [])
    results = []
    for i in inputs:
        result = longest_palindromic_arrangement(i)
        results.append(result)
    return jsonify({"answer": results})


if __name__ == '__main__':
    app.run(debug=True)
