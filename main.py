import sys
import argparse
from pycatfd import catfd_formain as catfd
#from Face_Morph import face_morph_main as face_morph
from Detect_Human_Facial_Features import detect_human as humanfd

def main():
    parser = argparse.ArgumentParser()

    #input images
    parser.add_argument("-c", "--cat", required=True, help="Enter filename of Cat")
    parser.add_argument("-human", "--human", required=True, help="Enter filename of Human")


    args = parser.parse_args()
    print(args)
    cat_image = args.cat
    human_image = args.human
    

    #Get cat features
    cat_features = catfd.detect(cat_image)
    #Get human features
    human_features = humanfd.detect(human_image)
    print(cat_features)
    print(human_features)
    #TODO: Get proper aligned features into file to test with face_morph

if __name__ == '__main__':
    main()