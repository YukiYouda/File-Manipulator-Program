import sys

input_contents = ''
revese_contents = ''
replace_contents = ''

if len(sys.argv) == 4 or len(sys.argv) == 5:
    input_path_name = sys.argv[2]
    # reverseコマンドの時
    if sys.argv[1] == 'reverse':
        output_path_name = sys.argv[3]
        with open(input_path_name) as f:
            input_contents = f.read()
            revese_contents = input_contents[::-1]

        with open(output_path_name, 'w') as f:
            f.write(revese_contents)

    # copyコマンドの時
    elif sys.argv[1] == 'copy':
        output_path_name = sys.argv[3]
        with open(input_path_name) as f:
            input_contents = f.read()

        with open(output_path_name, 'w') as f:
            f.write(input_contents)

    # duplicate-contentsコマンドのとき
    elif sys.argv[1] == 'duplicate-contents':
        duplicate_count = int(sys.argv[3])
        with open(input_path_name) as f:
            input_contents = f.read()

        with open(input_path_name, 'a') as f:
            for i in range(duplicate_count):
                f.write(input_contents)

    # replace-stringコマンドのとき
    elif sys.argv[1] == 'replace-string':
        before_string = sys.argv[3]
        after_string = sys.argv[4]
        with open(input_path_name) as f:
            input_contents = f.read()
            replace_contents = input_contents.replace(before_string, after_string)

        with open(input_path_name, 'w') as f:
            f.write(replace_contents)
    else:
        print('コマンド名が間違っています')
else:
    print('引数の数が間違っています')
