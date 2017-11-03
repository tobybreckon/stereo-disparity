#####################################################################

# correlate : cycle through a set of images from a directory
# and print out the file names of images that strongly correlate with
# the one before it (i.e. not much, if anything has changed)

# For use with provided test / training datasets

# Author : Toby Breckon, toby.breckon@durham.ac.uk

# Copyright (c) 2017 School of Engineering & Computing Science,
#                    Durham University, UK
# License : LGPL - http://www.gnu.org/licenses/lgpl.html

#####################################################################

import cv2
import os
from itertools import tee

directory_to_cycle = "/tmp/TTBB-durham-02-10-17-sub5" # edit this
image_wait_delay_time = 2;
display_images = True;

# for road traffic scene on a vehicle mounted camera 0.999 seems a good
# value to catch action/changes when vehicle is stationary but still
# remove shots with no difference in them

CORRELATION_THRESHOLD = 0.999 # correlation threshold (high is similar)

#####################################################################

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#####################################################################

# display all images in directory (sorted by filename)

files = sorted(os.listdir(directory_to_cycle))

# iterate throough them pairwise as per
# https://stackoverflow.com/questions/5764782/iterate-through-pairs-of-items-in-a-python-list

for filename_first, filename_next in pairwise(files):

    # print('first ' + os.path.join(directory_to_cycle, filename_first));
    # print('second ' + os.path.join(directory_to_cycle, filename_next));

    # if it is a PNG file

    if '.png' in filename_first:

        # read in images and display in a window

        img_first = cv2.imread(os.path.join(directory_to_cycle, filename_first), cv2.IMREAD_COLOR)
        img_next = cv2.imread(os.path.join(directory_to_cycle, filename_next), cv2.IMREAD_COLOR)

        if (display_images):
            cv2.imshow('image first', img_first)
            cv2.imshow('image next', img_next)

            key = cv2.waitKey(image_wait_delay_time) # wait N ms
            if (key == ord('x')):
                break

        # perform normalised cross-correlation on the current frame and the
        # next one (see forumulae for TM_CCOEFF_NORMED flag in OpenCV manual)

        # based on example at:
        # https://github.com/tobybreckon/python-examples-ip/blob/master/correlation_template_matching.py

        correlation = cv2.matchTemplate(img_first,img_next,cv2.TM_CCOEFF_NORMED);
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(correlation);

        if ((max_val) > CORRELATION_THRESHOLD):

            # print out second file name only such that we keep the first file

             print('correlation = '+ str(max_val) + ':' + os.path.join(directory_to_cycle, filename_next));

# close all windows

cv2.destroyAllWindows()

#####################################################################
