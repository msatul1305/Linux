from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                          format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)


def longest_palindromic_arrangement(files):
    answer = 'NULL'
    return {"answer": answer}


@app.route('/file-reorganization', methods=['POST'])
def file_reorganization():
    try:
        data = request.get_json()
        logging.info(data)
        if "inputs" in data and isinstance(data["inputs"], list):
            result = longest_palindromic_arrangement(data["inputs"])
            return jsonify(result)
        else:
            return jsonify({"error": "Invalid input format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
