from terminal.shell import Shell

exit_commands = ["exit", "quit", "q", "bye", "goodbye", "stop", "end", "finish", "done"]

def main():
    chat = Shell()
    while (q := chat.input()) not in exit_commands:
        chat(q)