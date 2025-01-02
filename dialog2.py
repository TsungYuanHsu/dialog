# Process LINE-Viki.txt

# Read function from LINE-Viki.txt
def read(filename):
    dialog = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            dialog.append(line.strip())
        return dialog


# Count words
def count(dialog):
    pair_dialog = []
    word_counter_Allen = 0
    word_counter_Viki = 0
    emoji_counter_Allen = 0
    emoji_counter_Viki = 0
    pic_counter_Allen = 0
    pic_counter_Viki = 0
    for content in dialog:
        pair_dialog.append(content.split(' ', 2))
    for line in pair_dialog:
        if line[1] == 'Allen':
            if line[2] == '貼圖':
                emoji_counter_Allen += 1
            elif line[2] == '圖片':
                pic_counter_Allen += 1
            else:
                word_counter_Allen = word_counter_Allen + len(line[2]) - line[2].count(' ')
        elif line[1] == 'Viki':
            if line[2] == '貼圖':
                emoji_counter_Viki += 1
            elif line[2] == '圖片':
                pic_counter_Viki += 1
            else:
                word_counter_Viki = word_counter_Viki + len(line[2]) - line[2].count(' ')
    print('Allen said', word_counter_Allen, 'words')
    print('Allen sent', emoji_counter_Allen, 'emojis')
    print('Allen sent', pic_counter_Allen, 'pictures')
    print('Viki said', word_counter_Viki, 'words')
    print('Viki sent', emoji_counter_Viki, 'emojis')
    print('Viki sent', pic_counter_Viki, 'pictures')


# Write function to output.txt
def write(filename, pair_dialog):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for pair in pair_dialog:
            f.write(pair[0] + ': ' + pair[1] + '\n')

def main():
    dialog = read('LINE-Viki.txt')
    count(dialog)
    # write('LINE-Viki-output.txt', pair_dialog)

main()