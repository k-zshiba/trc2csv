import os, tkinter, tkinter.filedialog

root = tkinter.Tk()
root.withdraw()
file_type = [(".trc","*")]
script_dir = os.path.abspath(os.path.dirname(__file__))
trc_files =  tkinter.filedialog.askopenfilenames(filetypes = file_type,initialdir = script_dir)

for trc_file in trc_files:
    print(trc_file, end ='')
    if trc_file.endswith('.trc'):
        file_name = os.path.splitext(trc_file)[0]
        with open(trc_file, 'r') as f:
            file_text = f.read()
            replaced_text = file_text.replace('\t',',')
            csv_file_path = file_name + ".csv"
            print(csv_file_path)
        with open(csv_file_path, 'w') as csv_file:
            csv_file.write(replaced_text)
    print(" [Done!]")
print("Finish converting trc to csv!!")
print("Enter the key to close this window")
a = input()