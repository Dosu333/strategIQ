from collections import deque


class AgentMemory:
    def __init__(self, max_length=5):
        self.history = deque(maxlen=max_length)

    def add(self, role, message):
        self.history.append({"role": role, "message": message})

    def get_context(self):
        return "\n".join([
            f"{h['role']}: {h['message']}" for h in self.history
        ])
