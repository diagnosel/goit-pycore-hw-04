import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_tree(path, level = 0):
    for item in path.iterdir():
        indent = "  " * level

        if item.is_dir():
            print(Fore.BLUE + indent + "📂 "+ item.name)
            print_tree(item, level + 1)
        else:
            print(Fore.GREEN + indent + "📜 " + item.name)
    
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 task_3.py <directory_path>")
        return
    
    path = Path(sys.argv[1])
    
    if not path.exists():
        print("Path does not exist")
        return
    
    if not path.is_dir():
        print("Path is not a directory")
        return

    print_tree(path)
    
if __name__ == "__main__":
    main()
    