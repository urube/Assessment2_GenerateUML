"""
cli will have the cmd interface
to-do: Make cmd robust for when users enter unknown codes
validate data: checking is source file is python or is classes are correct
"""
import cmd
from classes import Hospital, Doctor, Nurse


class CommandLineInterface(cmd.Cmd):
    intro = 'Simple Cli for Assessment2. Please type help or ? for command list.\n'
    prompt = '>>>'
    file = None

    def do_introduce(self, employee_name):
        """
        Syntax: introduce [name]
        follow the prompt.h
        """
        if employee_name == 'me':
            try:
                print('Welcome')
                name = (input("Please enter you employee_name: "))
                print('Hello ' + name)
            except ValueError as e:
                print(f'The exception is: {e}')
            except KeyError as e:
                print(f'{e}: Not a command')
            finally:
                print('Type help or ? to see more available commands.')
        else:
            message = "Incorrect syntax. Type: [Introduce me]"
            print(message)

    # def do_unpickle(self):
    #     from unpickle import Unpickle

    def do_load(self):
        """
        load the save uml file
        :return:
        """

    def do_exit(self, line):
        """
        Stop the program
        syntax: exit
        """
        print('Thank you for visiting.')
        return True


if __name__ == '__main__':
    CommandLineInterface().cmdloop()
