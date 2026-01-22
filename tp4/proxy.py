from flask import Flask, request, jsonify
import queue

app = Flask(__name__)

jobs_pending = queue.Queue()
jobs_done = queue.Queue()

@app.route("/task_queue", methods=["GET", "POST"])
def manage_tasks():
    if request.method == "POST":
        data = request.json
        jobs_pending.put(data)
        return "OK", 200
    try:
        current_job = jobs_pending.get_nowait()
        return jsonify(current_job)
    except queue.Empty:
        return jsonify(None)

@app.route("/result_queue", methods=["GET", "POST"])
def manage_results():
    if request.method == "POST":
        res_data = request.json
        jobs_done.put(res_data)
        return "OK", 200
    try:
        final_res = jobs_done.get_nowait()
        return jsonify(final_res)
    except queue.Empty:
        return jsonify(None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)