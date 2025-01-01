# Read input.txt file and write into output.txt file

# Read function from input.txt
def read(filename):
    dialog = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            dialog.append(line.strip())
        return dialog

# Pair function to pair content with name
def pair(dialog):
    name = None
    pair_dialog = []
    for content in dialog:
        if 'Allen' in content:
            name = 'Allen'
            continue
        elif 'Tom' in content:
            name = 'Tom'
            continue
        else:
            pair_dialog.append([name, content])
    return pair_dialog

# Write function to output.txt
def write(filename, pair_dialog):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for pair in pair_dialog:
            f.write(pair[0] + ': ' + pair[1] + '\n')

def main():
    dialog = read('input.txt')
    pair_dialog = pair(dialog)
    write('output.txt', pair_dialog)

main()