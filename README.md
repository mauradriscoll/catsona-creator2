# catsona-creator2

How to Create Your Own Catsona:

To use, open catsona-creator2 as well as a terminal. 
Create a virtual enviornment using our requirements.txt file and activate. 
Upload the desired catsona image and human image so that they are in the catsona-creator2 folder. 
In the terminal type "python main.py" along with the following flags:
    -human: followed by filename of human image
    -catsona: followed by file name of cat image
    -fs: to turn on face swap (without this flag the image that will appear will only be 
    the morphed cat and human face, not back on the orignal catsona)
    -cat: find the feature points of cat image and attempt to morph with human image 
    (leftover from our previous attempt at the implementation, however the feature points 
    we obtain for cats are still pretty accurate, only the morphed image will be very distorted)
    -alpha: if desired, the user can specify their own alpha level if the catsona is not as 
    well blended as desired (value 0-1)
    
  
