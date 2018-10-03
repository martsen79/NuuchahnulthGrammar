import os, sys

'''item:
  i-id :integer :key
  i-origin :string
  i-register :string
  i-format :string
  i-difficulty :integer
  i-category :string
  i-input :string
  i-tokens :string
  i-gloss :string
  i-translation :string
  i-wf :integer
  i-length :integer
  i-comment :string
  i-author :string
  i-date :date'''

'''Assuming input file has Speaker tab plaintext tab IGT (tab translation)'''
def generate_item_file(input_file_path, output_file_path):
    input_file = open(input_file_path).readlines()
    output = []
    key = 1
    for line in input_file:
        line_split = line.strip().split('\t')
        if len(line_split) < 3:
            print('Error on following line, improperly formatted:\n' + line)
            continue
        id = str(key)
        origin = line_split[0]
        register = ''
        format = ''
        difficulty = '1'
        category = ''
        input = line_split[2].strip('*').strip('?')
        tokens = ''
        gloss = ''
        translation = ''
        if len(line_split) == 4:
            translation = line_split[3]
        wf = '1'
        if '*' in line_split[2]:
            wf = '0'
        length = str(len(line_split[2].strip().split()))
        comment = ''
        author = 'davinman'
        date =''
        output.append(id + '@' + origin + '@' + register + '@' + format + '@' + difficulty \
         + '@' + category + '@' + input + '@' + tokens + '@' + gloss + '@' + translation \
         + '@' + wf + '@' + length + '@' + comment + '@' + author + '@' + date + '\n')
        key += 1
    output_file = open(output_file_path, 'w+')
    output_file.writelines(output)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(sys.argv)
        print('Please pass in (1) the path for the file to read, (2) the path for the output')
    else:
        generate_item_file(sys.argv[1], sys.argv[2])