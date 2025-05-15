from flask import Flask, jsonify, request
from ml_package import question2 as q2
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the ML Package API!"

@app.route("/functions")
def list_functions():
    return jsonify([func for func in dir(q2) if not func.startswith("_")])

def serialize(obj):
    """Convert NumPy types to native Python types."""
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (np.float64, np.int64)):
        return obj.item()
    elif isinstance(obj, dict):
        return {k: serialize(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize(v) for v in obj]
    else:
        return obj

def handle_process(problem, n_samples, n_features):
    X, y = q2.generate(problem, n_samples, n_features)
    stats = q2.statistics(X, y)
    model, error = q2.learn(problem, X, y)
    preds = q2.predict(model, problem)

    return serialize({
        "problem": problem,
        "error": error,
        "statistics": stats,
        "predictions": preds
    })

@app.route("/process")
def process():
    n_samples = int(request.args.get("n_samples", 100))
    n_features = int(request.args.get("n_features", 5))
    problem = request.args.get("problem", "classification")
    return jsonify(handle_process(problem, n_samples, n_features))

@app.route("/classification/process")
def classification_process():
    n_samples = int(request.args.get("n_samples", 100))
    n_features = int(request.args.get("n_features", 5))
    return jsonify(handle_process("classification", n_samples, n_features))

@app.route("/regression/process")
def regression_process():
    n_samples = int(request.args.get("n_samples", 100))
    n_features = int(request.args.get("n_features", 5))
    return jsonify(handle_process("regression", n_samples, n_features))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
