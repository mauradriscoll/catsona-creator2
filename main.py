import sys
import argparse
import cv2
from pycatfd import catfd_formain as catfd
#from Face_Morph import face_morph_main as face_morph
from Detect_Human_Facial_Features import detect_human as humanfd

def main():
    parser = argparse.ArgumentParser()

    #input images
    parser.add_argument("-c", "--cat", help="Enter filename of Cat")
    parser.add_argument("-human", "--human", required=True, help="Enter filename of Human")
    parser.add_argument("-catsona", "--catsona",  help="Enter filename of catsona")


    args = parser.parse_args()
    cat_image = args.cat
    human_image = args.human
    catsona_image = args.catsona

    

    #Get cat features
    cat_features = catfd.detect(cat_image)
    #print(cat_features[0][0])
    #Get human features
    human_features = humanfd.detect(human_image)
    #catsona_features = humanfd.detect(catsona_image)
    fh = open(human_image + '.txt', "w")
    fc = open(cat_image + '.txt', "w")
    #write human features to a file to be interpreted by face morph
    for part in human_features:
        for point in human_features[part]:
            fh.write(str(point[0]) + " " + str(point[1])+"\n")
    fh.close()
    #write cat features to a file that can be interpreted by Face Morph
    for part in cat_features[0]['face']['landmarks']:   
        point =  cat_features[0]['face']['landmarks'][part]
        print(point)
        fc.write(str(point[0]) + " " + str(point[1])+"\n")
    fc.close()
    
    #TODO: Get proper aligned features into file to test with face_morph

if __name__ == '__main__':
    main()