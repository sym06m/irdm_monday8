class SessionContext:
    def __init__(self):
        self.history = []

    def add(self, message):
        self.history.append(message)

    def get_context(self):
        return " ".join(self.history)


session = SessionContext()
session.add("User wants a business plan.")
session.add("Budget is limited.")

print(session.get_context())
