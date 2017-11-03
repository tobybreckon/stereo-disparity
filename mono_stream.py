#####################################################################

# Example : load, display and cycle the ** left or right only ** image from a
# for a set of rectified stereo images from a  directory structure
# of left-images / right-images with filesname DATE_TIME_STAMP_{L|R}.png

# optionally load available IMU/GPS ground truth data

# basic illustrative python script for use with provided dataset

# Author : Toby Breckon, toby.breckon@durham.ac.uk

# Copyright (c) 2017 Department of Computer Science,
#                    Durham University, UK
# License : LGPL - http://www.gnu.org/licenses/lgpl.html

#####################################################################

import cv2
import os
import numpy as np
import csv
import gyro     # local file gyro.py

#####################################################################

# where is the data ? - set this to where you have it

master_path_to_dataset = "/tmp/TTBB-durham-02-10-17-sub5"; # ** need to edit this **
directory_to_cycle = "left-images";     # edit this for left or right image set

#####################################################################

# full camera parameters - from camera calibration
# supplied images are stereo rectified

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

# open ground truth GPS / IMU data files if available

gps_file_name = os.path.join(master_path_to_dataset, "GPS.csv");
imu_file_name = os.path.join(master_path_to_dataset, "IMU.csv");
gps_data = [];
imu_data = [];

if (os.path.isfile(gps_file_name)):
    with open(gps_file_name, newline='') as csvfileGPS:
        gps_data = list(csv.DictReader(csvfileGPS));
        print("-- using GPS data file: " + gps_file_name);
else:
        print("-- GPS data file not found: " + gps_file_name);

if (os.path.isfile(imu_file_name)):
    with open(imu_file_name, newline='') as csvfileIMU:
        imu_data = list(csv.DictReader(csvfileIMU));
        print("-- using IMU data file: " + imu_file_name);
else:
        print("-- IMU data file not found: " + imu_file_name);

# get a list of the files, sort them (by timestamp in filename) and iterate

for index, filename in enumerate(sorted(os.listdir(full_path_directory))):

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

        print("-- file loaded successfully");
        print("\n");

        #####################################################################

        # *** do any processing here ***

        #####################################################################

        # for now diplay GPS/IMU data on image if we have it

        if (len(gps_data) >= index):
            text = "GPS: lat.=%2f long.=%2f alt.=%2f"\
                %(float(gps_data[index]['latitude']),
                float(gps_data[index]['longitude']),
                float(gps_data[index]['altitude']));
            cv2.putText(img, text, (20,40), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1, 12)

        if (len(imu_data) >= index):

            roll, pitch, heading = gyro.gyro_to_angles(
                        float(imu_data[index]['orientation_x']),
                        float(imu_data[index]['orientation_y']),
                        float(imu_data[index]['orientation_z']),
                        float(imu_data[index]['orientation_w']));

            text = "IMU: roll/pitch/heading. (%2f, %2f, %2f) "\
                %(roll, pitch, heading);
            cv2.putText(img, text, (20,60), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1, 12)

            text = "IMU: angular velocity (%2f, %2f, %2f)"\
                %(float(imu_data[index]['angular_velocity_x']),
                float(imu_data[index]['angular_velocity_y']),
                float(imu_data[index]['angular_velocity_z']));
            cv2.putText(img, text, (20,80), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1, 12)

            text = "IMU: accel. (%2f, %2f, %2f)"\
                %(float(imu_data[index]['linear_acceleration_x']),
                float(imu_data[index]['linear_acceleration_y']),
                float(imu_data[index]['linear_acceleration_z']));
            cv2.putText(img, text, (20,100), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1, 12)

        # display the image

        cv2.imshow('input image',img);

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
