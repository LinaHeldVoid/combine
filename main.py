import os

FILE1_PATH = "1.txt"
BASE1_PATH = os.getcwd()
txt1_path = os.path.join(BASE1_PATH, FILE1_PATH)

FILE2_PATH = "2.txt"
BASE2_PATH = os.getcwd()
txt2_path = os.path.join(BASE2_PATH, FILE2_PATH)

FILE3_PATH = "3.txt"
BASE3_PATH = os.getcwd()
txt3_path = os.path.join(BASE3_PATH, FILE3_PATH)

FILE4_PATH = "4.txt"
BASE4_PATH = os.getcwd()
txt4_path = os.path.join(BASE4_PATH, FILE4_PATH)

file_names = []
file_names.append(FILE1_PATH)
file_names.append(FILE2_PATH)
file_names.append(FILE3_PATH)

def combine():
    with open (txt1_path) as txt1, open(txt2_path) as txt2, open(txt3_path) as txt3:
        combined_text = {}
        text_list = []
        text_list.append(txt1)
        text_list.append(txt2)
        text_list.append(txt3)
        k = 0
        for i in text_list:
            for line in i:
                combined_text.setdefault(file_names[k], [])
                combined_text[file_names[k]].append(line)
            k += 1


        new_dict = dict(sorted(combined_text.items(), key = lambda x: x[1]))

        with open(txt4_path, 'w') as txt4:
            for i in new_dict.keys():
                volume = len(new_dict.get(i))
                txt4.write(f'{i}' + '\n')
                txt4.write(f'{str(volume)}' + '\n')
                for k in new_dict.get(i):
                    txt4.write(f'{k}')
                txt4.write('\n' + '\n')

        with open(txt4_path, 'r') as txt4:
            for line in txt4:
                print(line)

combine()