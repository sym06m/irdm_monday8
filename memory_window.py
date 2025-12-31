class MemoryBuffer:
    def __init__(self, limit=3):
        self.limit = limit
        self.buffer = []

    def add(self, message):
        self.buffer.append(message)
        if len(self.buffer) > self.limit:
            self.buffer.pop(0)

    def read(self):
        return self.buffer


memory = MemoryBuffer()

memory.add("User wants marketing advice")
memory.add("Target audience is students")
memory.add("Budget is small")
memory.add("Location is urban")

print(memory.read())
