from SQLYacc import parser, operations

if __name__ == "__main__":
    info = '(None)> '
    while True:
        try:
            s = raw_input(info)
        except EOFError:
            break
        if not s:
            continue
        parser.parse(s)
        operations.pop_queue()
        info = "(%s)> " % str(operations.Fun.currentdb)