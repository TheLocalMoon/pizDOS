# main.py #
import os

version = 0.1
commands = {
  "help": "shows this",
  "say": "says whatever you want",
  "calc": "calculator11!!1!",
  "clear": "cleans the screen"
}

print(f"pizDOS {version}")
print("type help for list of commands")

while True:
  command = input("> ").lower()
  split_input = command.split(maxsplit=1)

  command = split_input[0]
  
  match command:
    case "help":
      for cmd, desc in commands.items():
        print(f'{cmd} - {desc}')
    case "say":
      if len(split_input) > 1:
        text = split_input[1]
        print(text)
      else:
        print('mafaka you must provide text <:(')
    case "calc":
      print("welcome to calculator")
      while True:
        calculation = input(">> ").lower()
        match calculation:
          case "exit":
            print("welcome back to pizDOS")
            break
          case _:
            try:
              print(eval(calculation))
            except (SyntaxError, NameError, ZeroDivisionError):
              print('invalid calculation')
    case "clear":
      if os.name == "nt":
        os.system('cls')
      else:
        os.system('clear')
    case _:
      print(f'unknown command: \"{command}\", type \"help\" for list of commands')