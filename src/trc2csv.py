import os

trc_file_folder = "../trcFolder"
csv_file_folder = "../csvFolder/"

trc_files =  os.listdir(trc_file_folder)
for trc_file in trc_files:
    trc_file_path = trc_file_folder + "/" + trc_file
    print(trc_file, end ='')
    if trc_file_path.endswith('.trc'):
        file_name = os.path.splitext(os.path.basename(trc_file))[0]
        with open(trc_file_path, 'r') as f:
            file_text = f.read()
            replaced_text = file_text.replace('\t',',')
            csv_file_path = csv_file_folder + file_name + ".csv"
        with open(csv_file_path, 'w') as csv_file:
            csv_file.write(replaced_text)
    print(" [Done!]")
print("Finish converting trc to csv!!")
print("Enter the key to close this window")
a = input()