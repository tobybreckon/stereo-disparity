#####################################################################

# Example : load and display the ** left or right only ** image from a
# for a set of rectified stereo images from a  directory structure
# of left-images / right-images with filesname DATE_TIME_STAMP_{L|R}.png

# basic illustrative python script for use with provided dataset

# Author : Toby Breckon, toby.breckon@durham.ac.uk

# Copyright (c) 2017 Department of Computer Science,
#                    Durham University, UK
# License : LGPL - http://www.gnu.org/licenses/lgpl.html

#####################################################################

import cv2
import os
import numpy as np

#####################################################################

# where is the data ? - set this to where you have it

master_path_to_dataset = "/tmp/durham-02-10-17"; # ** need to edit this **
directory_to_cycle = "left-images";     # edit this for left or right image set

#####################################################################

# full camera parameters - from camera calibration

camera_focal_length_px = 399.9745178222656;  # focal length in pixels (fx, fy)
camera_focal_length_m = 4.8 / 1000;          # focal length in metres (4.8 mm, f)
stereo_camera_baseline_m = 0.2090607502;     # camera baseline in metres (B)
camera_height_above_wheelbase_m = (1608.0 + 31.75 + 90) / 1000; # in mm

optical_image_centre_h = 262.0;             # from calibration - cy
optical_image_centre_w = 474.5;             # from calibration - cx

image_height = 544;
image_width = 1024;

#####################################################################

# set this to a file timestamp to start from (empty is first example - outside lab)
# e.g. set to 1506943191.487683 for the end of the Bailey, just as the vehicle turns

skip_forward_file_pattern = ""; # set to timestamp to skip forward to

pause_playback = False; # pause until key press after each image

#####################################################################

# resolve full directory location of data set for images

full_path_directory =  os.path.join(master_path_to_dataset, directory_to_cycle);

# get a list of the files, sort them (by timestamp in filename) and iterate

for filename in sorted(os.listdir(full_path_directory)):

    # skip forward to start a file we specify by timestamp (if this is set)

    if ((len(skip_forward_file_pattern) > 0) and not(skip_forward_file_pattern in filename)):
        continue;
    elif ((len(skip_forward_file_pattern) > 0) and (skip_forward_file_pattern in filename)):
        skip_forward_file_pattern = "";

    # from image filename get the correspondoning full path

    full_path_filename = os.path.join(full_path_directory, filename);

    # for sanity print out these filenames

    print(full_path_filename);

    # check the file is a PNG file (left) and check a correspondoning right image
    # actually exists

    if ('.png' in filename) and (os.path.isfile(full_path_filename)) :

        # read left and right images and display in windows
        # N.B. despite one being grayscale both are in fact stored as 3-channel
        # RGB images so load both as such

        img = cv2.imread(full_path_filename, cv2.IMREAD_COLOR)
        cv2.imshow('input image',img)

        print("-- file loaded successfully");
        print("\n");

        #####################################################################

        # *** do any processing here ***

        #####################################################################

        # keyboard input for exit (as standard), save disparity and cropping
        # exit - x
        # save - s
        # pause - space

        key = cv2.waitKey(40 * (not(pause_playback))) & 0xFF; # wait 40ms (i.e. 1000ms / 25 fps = 40 ms)
        if (key == ord('x')):       # exit
            break; # exit
        elif (key == ord('s')):     # save
            cv2.imwrite("input.png", img);
        elif (key == ord(' ')):     # pause (on next frame)
            pause_playback = not(pause_playback);
    else:
            print("-- files skipped (perhaps one is missing or not PNG)");
            print("\n");

# close all windows

cv2.destroyAllWindows()

#####################################################################
