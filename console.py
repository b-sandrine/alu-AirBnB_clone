#!/usr/bin/env python3
"""
HBNB Console Application

Minimal interactive console using Python's built-in cmd module.
Provides placeholder commands for listing and adding places.
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    intro = "Welcome to the HBNB console. Type help or ? to list commands."

    # ----- basic commands -----
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D on Unix/macOS, Ctrl+Z then Enter on Windows)."""
        print()  # newline for clean prompt return
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    # ----- placeholder feature commands -----
    def do_list_places(self, arg):
        """List all available places (placeholder).

        Usage: list_places
        """
        # TODO: Replace with real DB retrieval from Postgres
        print("[placeholder] Listing places (connect to Postgres in future).")

    def do_add_place(self, arg):
        """Add a place (placeholder).

        Usage: add_place <name>
        """
        name = arg.strip()
        if not name:
            print("Error: place name is required. Usage: add_place <name>")
            return
        # TODO: Replace with real DB insert into Postgres
        print(f"[placeholder] Added place: {name}")


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    shell = HBNBCommand()
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()
