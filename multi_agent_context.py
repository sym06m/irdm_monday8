class ContextStore:
    def __init__(self):
        self.shared_context = {}

    def update(self, key, value):
        self.shared_context[key] = value

    def get(self, key):
        return self.shared_context.get(key)


class Agent:
    def __init__(self, name, context_store):
        self.name = name
        self.context = context_store

    def run(self, input_text):
        self.context.update(self.name, input_text)
        return f"{self.name} processed input"


context_store = ContextStore()

agent_a = Agent("planner", context_store)
agent_b = Agent("executor", context_store)

print(agent_a.run("Create a strategy"))
print(agent_b.run(context_store.get("planner")))
