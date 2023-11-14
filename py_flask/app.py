from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                          format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)


def longest_palindromic_arrangement(inp):
    names = inp[1].split()
    pairs = inp[2:]
    logging.info(names)
    data_dict = {}
    for i, name in enumerate(names):
        key, value = map(int, pairs[i].split())
        data_dict[name] = (key, value)
    values = inp[2:2+int(inp[0])]
    x = []
    for val in values:
        x.append(int(val.split(" ")[0]))
        x.append(int(val.split(" ")[1]))
    y = list(set(x))
    y.sort()
    lis = [f'{inp[0]}']
    for k in range(len(y)-1):
        op1 = f'{y[k]} {y[k+1]}'
        count = 0
        names = []
        for key, val in data_dict.items():
            if val[0] <= y[k] and val[1] >= y[k+1]:
                count = count + 1
                names.append(key)
                names.sort()
        listToStr = ' '.join([str(elem) for i, elem in enumerate(names)])
        op2 = f'{count} {listToStr}'
        op = f'{op1} {op2}'
        lis.append(op)
    return lis


@app.route('/file-reorganization', methods=['POST'])
def file_reorganization():
    data = request.json
    inputs = data.get('inputs', [])
    results = []
    result = longest_palindromic_arrangement(inputs)
    results.append(result)
    return jsonify({"answer": results})


if __name__ == '__main__':
    app.run(debug=True)
