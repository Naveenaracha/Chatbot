from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from get_answer import get_answer

app = Flask(__name__)

CORS(app)

@app.route("/solve_doubt", methods=['POST'])
def solve_doubt():
    try:
        data = request.get_json()
        user_question = data.get("question")

        if not user_question:
            return jsonify({"error": "Question not provided"}), 400
        
        solution = get_answer(user_question)

        return jsonify({"solution": solution})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True)