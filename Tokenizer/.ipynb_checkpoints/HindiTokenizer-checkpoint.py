#Before Tokenizing Install Packages or You can create your own Tokenizer

#pip install inltk
#pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
import re

with open("./Data/News.txt",'r') as f:
    arr=f.read;
    
print(arr)
