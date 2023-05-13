
class Memory:
    _memory = list()

    def __getitem__(self, index):
        return self._memory[index]

    def __repr__(self):
        return self._memory

    def __str__(self):
        return str(self._memory)

    def add(self, role, message, recording=None, user_recording=None):
        self._memory.append({"role": role, "content": message, "recording": recording,
                             "user_recording": user_recording})

    def get_chat_history(self):
        return [{"role": message["role"], "content": ' '.join(message["content"].split())} for message in self._memory]