from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task list (later can be DB)
tasks = []

@app.route("/")
def home():
    return "✅ Task Bot is running!"

@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {"id": len(tasks)+1, "task": data.get("task"), "status": "pending"}
    tasks.append(task)
    return jsonify({"message": "Task added", "task": task})

@app.route("/list", methods=["GET"])
def list_tasks():
    return jsonify(tasks)

@app.route("/done/<int:task_id>", methods=["POST"])
def mark_done(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
            return jsonify({"message": "Task marked as done", "task": t})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
