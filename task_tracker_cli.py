import functions as funcs
import sys

def main():
    if len(sys.argv) < 2:
        print("Type 'help' for information about usage. ")
        return
    
    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) == 3:
        funcs.add_task(sys.argv[2])

    elif command == "update" and len(sys.argv) == 4:
        funcs.update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete" and len(sys.argv) == 3:
        funcs.delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress" and len(sys.argv) == 3:
        funcs.mark_task(int(sys.argv[2]), "in-progress")

    elif command == "mark-done" and len(sys.argv) == 3:
        funcs.mark_task(int(sys.argv[2]), "done")

    elif command == "show":
        funcs.show_tasks()

    elif command == "help":
        print("coming soon")

    else:
        print("Invalid command or arguments.")

if __name__ == "__main__":
    main()




"""funcs.add_task("Finish your first roadmap.sh project")

funcs.show_tasks()

funcs.delete_task(1)

funcs.show_tasks()

sys.argv[2].lower() if len(sys.argv) == 3 else None
"""