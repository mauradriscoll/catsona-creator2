import sys
import argparse
from pycatfd import catfd_formain as catfd
#from Face_Morph import face_morph as face_morph
#from Detect_Human_Facial_Features import detect_face_features as humanfd

def main():
    parser = argparse.ArgumentParser()

    #input images
    parser.add_argument("-c", "--cat", required=True, help="Enter filename of Cat")
    #parser.add_argument("-h", "--human", required=True, help="Enter filename of Human")


    args = parser.parse_args()
    #print(args)
    cat_image = args.cat
    #print(cat_image)
    #human_image = args.human

    #Get cat features

    cat_features = catfd.detect(cat_image)
    print(cat_features)

if __name__ == '__main__':
    main()