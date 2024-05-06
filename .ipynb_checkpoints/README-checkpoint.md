# NER_CRF_Hindi
This is the Project, I have been assigned in Semester 2 for Computational Linguistics Course.

###All of the Models are based on CRF (It includes Chunking,POS,NER)
####Install CRF from "https://taku910.github.io/crfpp/#download"
####Run Following command while in CRF folder:
    ./config
    make
    sudo make install

    For more Information: https://www.youtube.com/watch?v=6b3DmE2jYzg
    
###For Tokenizing We used prebuilt model from iNLTK, but can be done using Regex and Python,(Sample Code provided for English)

Source of NER Data: "ai4bharat/naamapadam" from HuggingFace
Source of POS Data: Hugging Face
Source of Chunking: Missing(I had to do)
Source of Test Data: News:AajTak,Amar Ujala
                     Story: Do Bail -PremChand

The Genre of NER Training Data is mixed, whereas POS is some Article or Story.
    

