import sys
import argparse
import cv2
import numpy as np
from pycatfd import catfd_formain as catfd
from Face_Morph import face_morph_main as face_morph
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
    if cat_image is not None:
        cat_features = catfd.detect(cat_image)
    #print(cat_features[0][0])
    #Get human features
    
    if catsona_image is not None:
        catsona_features = humanfd.detect(catsona_image)
        fcc = open(catsona_image + '.txt', "w")
        for part in catsona_features:
            for point in catsona_features[part]:
                fcc.write(str(point[0]) + " " + str(point[1])+"\n")
        fcc.write(str(0) + " " + str(0) + "\n")
        fcc.write(str(497) + " " + str(0) + "\n")
        fcc.write(str(0) + " " + str(497) + "\n")
        fcc.write(str(497) + " " + str(497) + "\n")
        fcc.close()

    fh = open(human_image + '.txt', "w")
    human_features = humanfd.detect(human_image)
    #write human features to a file to be interpreted by face morph
    for part in human_features:
        for point in human_features[part]:
            fh.write(str(point[0]) + " " + str(point[1])+"\n")
    fh.write(str(0) + " " + str(0) + "\n")
    fh.write(str(497) + " " + str(0) + "\n")
    fh.write(str(0) + " " + str(497) + "\n")
    fh.write(str(497) + " " + str(497) + "\n")
    fh.close()
    #write cat features to a file that can be interpreted by Face Morph
    if cat_image is not None:
        fc = open(cat_image + '.txt', "w")
        for part in cat_features[0]['face']['landmarks']:   
            point =  cat_features[0]['face']['landmarks'][part]
            print(point)
            fc.write(str(point[0]) + " " + str(point[1])+"\n")
        fc.close()
    
    #TODO: Get proper aligned features into file to test with face_morph
    if catsona_image is not None:
        img = face_morph.morph(human_image, catsona_image)
    else:
        img = face_morph.morph(human_image, cat_image)

    # Display Result
    cv2.imshow("Morphed Face", np.uint8(img))
    cv2.waitKey(0)
if __name__ == '__main__':
    main()