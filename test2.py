import cmd


class Illustrate(cmd.Cmd):
    "Illustrate the base class method use."

    def cmdloop(self, intro=None):
        print(f'cmdloop({intro})')
        return super().cmdloop(intro)

    def preloop(self):
        print('preloop()')

    def postloop(self):
        print('postloop()')

    def parseline(self, line):
        print(f'parseline({line}) =>', end=' ')
        ret = super().parseline(line)
        print(ret)
        return ret

    def onecmd(self, s):
        print(f'onecmd({s})')
        return super().onecmd(s)

    def emptyline(self):
        print('emptyline()')
        return super().emptyline()

    def default(self, line):
        print(f'default({line})')
        if line == "hello":
            return self.do_greet(line)
        else:
            return super().default(line)

    def precmd(self, line):
        print(f'precmd({line})')
        return super().precmd(line)

    def postcmd(self, stop, line):
        print(f'postcmd({stop}, {line})')
        return super().postcmd(stop, line)

    def do_greet(self, line):
        print(f'hello, {line}')

    def do_EOF(self, line):
        "Exit"
        return True

    AVAILABLE_COLORS = ('blue', 'green', 'yellow', 'red', 'black')

    def complete_color(self, line):
        self.do_greet(line)  # or self.do_greet("some other string")


if __name__ == '__main__':
    Illustrate().cmdloop('Illustrating the methods of cmd.Cmd')
