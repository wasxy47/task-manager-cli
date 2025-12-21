import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

# --- ABDUL WASAY'S FEATURE: ADD TASK ---
def add_task(description):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "task": description, "status": "pending"})
    save_tasks(tasks)
    print(f"Task added: {description}")

if __name__ == "__main__":
    add_task("First task by Abdul Wasay")