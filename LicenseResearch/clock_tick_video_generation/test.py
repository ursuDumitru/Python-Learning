import os
import matplotlib.pyplot as plt
# %matplotlib inline
import matplotlib.image as mpimg

def print_in_color(txt_msg, fore_tupple, back_tupple):
    rf, gf, bf = fore_tupple
    rb, gb, bb = back_tupple
    msg='{0}' + txt_msg
    mat=('\33[38;2;' + str(rf) +';' + str(gf) + 
         ';' + str(bf) + ';48;2;' + str(rb) + 
         ';' +str(gb) + ';' + str(bb) +'m') 
    print(msg.format(mat))

sdir=r'./data/'
train_dir=os.path.join(sdir, 'train')

msg='{0:8s}{1:4s}{2:^28s}{1:4s}{3:8s}{1:3s}{4:8s}{1:3s}{5:7s}{6}'
msg=msg.format('ClassID', ' ', 'Clock Time ', 'Train', 'Test', 'Valid', '\n')
print_in_color(msg, (0, 255, 255), (0, 0, 0))

species_list=sorted(os.listdir(train_dir))
for i, specie in enumerate(species_list):
    file_path=os.path.join(train_dir, specie)
    train_files_list=os.listdir(file_path)
    train_file_count=str(len(train_files_list))
    
    msg='{0:^8s}{1:4s}{2:^28s}{1:4s}{3:^8s}{1:1s}{4:^8s}{1:3s}{5:^8s}'
    msg=msg.format(str(i), ' ', specie, train_file_count, '5', '5')
    
    toggle=i%2
    if toggle==0:
        back_color=(255,255,255)
    else:
        print(1)
        back_color=(191, 239, 242)

    print_in_color(msg, (0, 0, 0), back_color)
    