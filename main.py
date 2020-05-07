import sys
import argparse
import cv2
import numpy as np
import imutils
from pycatfd import catfd_formain as catfd
from Face_Morph import face_morph_main as face_morph
from Detect_Human_Facial_Features import detect_human as humanfd
from Face_Swap.face_swap_wrapper import fs_wrapper

def main():
    parser = argparse.ArgumentParser()

    #input images
    parser.add_argument("-c", "--cat", help="Enter filename of Cat")
    parser.add_argument("-human", "--human", required=True, help="Enter filename of Human")
    parser.add_argument("-catsona", "--catsona",  help="Enter filename of catsona")
    parser.add_argument("-fs", action='store_true', help="FaceSwap On")
    parser.add_argument("-alpha", "--alpha", help="If desired, provide alpha level to control blending range [0-1]", default = 0.15)


    args = parser.parse_args()
    cat_image = args.cat
    human_image = args.human
    catsona_image = args.catsona
    alpha = float(args.alpha)

    catsona_image_image = cv2.imread(catsona_image)
    human_image_image = cv2.imread(human_image)

    catsona_image_image = imutils.resize(catsona_image_image, width=500)
    human_image_image = imutils.resize(human_image_image, width=500)

    #Get cat features
    if cat_image is not None:
        cat_features = catfd.detect(cat_image)
    #if catsona is specified
    if catsona_image is not None:
        catsona_features = humanfd.detect(catsona_image)
        fcc = open(catsona_image + '.txt', "w")
        for part in catsona_features:
            for point in catsona_features[part]:
                fcc.write(str(point[0]) + " " + str(point[1])+"\n")
        fcc.write(str(0) + " " + str(0) + "\n")
        fcc.write(str(catsona_image_image.shape[1]-1) + " " + str(0) + "\n")
        fcc.write(str(0) + " " + str(catsona_image_image.shape[0]-1) + "\n")
        fcc.write(str(catsona_image_image.shape[1]-1) + " " + str(catsona_image_image.shape[0]-1) + "\n")
        fcc.close()

    fh = open(human_image + '.txt', "w")
    human_features = humanfd.detect(human_image)
    #write human features to a file to be interpreted by face morph
    for part in human_features:
        for point in human_features[part]:
            fh.write(str(point[0]) + " " + str(point[1])+"\n")
    fh.write(str(0) + " " + str(0) + "\n")
    fh.write(str(human_image_image.shape[1]-1) + " " + str(0) + "\n")
    fh.write(str(0) + " " + str(human_image_image.shape[0]-1) + "\n")
    fh.write(str(human_image_image.shape[1]-1) + " " + str(human_image_image.shape[0]-1) + "\n")
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
        img = face_morph.morph(human_image, catsona_image, alpha)
        if args.fs:
            img = fs_wrapper(np.uint8(img),catsona_image)
    else:
        img = face_morph.morph(human_image, cat_image, alpha)

    # Display Result
    cv2.imshow("Morphed Face", np.uint8(img))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()