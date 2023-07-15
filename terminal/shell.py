import os, subprocess

from rich.console import Console

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

from terminal.chain import history

class Shell:

    model = 'gpt-4'
    temperature = 0.3
    verbose = False
    history = history
    console = Console()

    def __init__(self) -> None:
        self.sensei = ChatOpenAI(
            model = self.model,
            temperature = self.temperature, 
            openai_api_key = os.environ.get("OPENAI_API_KEY")
        )
    
    def input(self):
        return self.console.input("[bold red]> [/]")
    
    def exec(self, command: str) -> None:
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            stdout, stderr = process.communicate()
            self.console.print(stdout)
            self.console.print(stderr)
        
        except subprocess.CalledProcessError as e:
            self.console.print("[bold red] Command execution failed. Return Code:", e.returncode)
            self.console.print("[bold red] Error Output:", e.output)

        except Exception as e:
            self.console.print("[bold red] An error occurred:", str(e))
    
    def __call__(self, query: str):
        self.history.append(
            HumanMessage(content = query)
        )

        response = self.sensei(self.history)
        self.history.append(response)

        if not response.content.startswith('`'):
            self.console.print(response.content)
            return
        
        commands = [response.content.replace('`','')]
        self.history.append(
            HumanMessage(content = '--next')
        )

        while (response := self.sensei(self.history)).content != "--done":
            commands.append(
                response.content.replace('`','')
            )

            self.history.append(response)
            self.history.append(
                HumanMessage(content = '--next')
            )
        
        self.history.append(response)

        self.console.print("Run the following commands?")
        self.console.print("\n".join(commands))

        if self.input().lower() == 'y':
            for command in commands:
                self.exec(command)
