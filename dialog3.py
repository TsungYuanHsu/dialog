# Practice dialog 3

# Read 3.txt
def read(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        dialog = []
        for line in f:
            line = line.strip('\n').split(' ', 1)
            content = line[1]
            time = line[0][:5]
            name = line[0][5:]
            dialog.append(time + ' ' + name + ' ' + content)
        return dialog
        

# Write into output file of 3.txt
def write(filename, dialog):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in dialog:
            f.write(line + '\n')


def main():
    dialog = read('3.txt')
    write('3_output.txt', dialog)

main()
