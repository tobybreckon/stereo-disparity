#####################################################################

# routine to convert (X,Y,Z,W) gyro output from a YotcoPuce 3D (3Dv2)
# sensor to roll, pitch and heading (compass)

# basic illustrative python script for use with provided dataset
# which originates from a YotcoPuce 3D (3Dv2) IMU sensor

# Author : Toby Breckon, toby.breckon@durham.ac.uk

# Copyright (c) 2017 Department of Computer Science,
#                    Durham University, UK
# License : LGPL - http://www.gnu.org/licenses/lgpl.html

#####################################################################

# acknowledgements: Yoctopuce Sarl, Switzerland.
# (yFindGyro(), the high-level API for Gyro functions)
# From: https://github.com/yoctopuce/yoctolib_python

# some portions of this code are under the following license:

#* Implements yFindGyro(), the high-level API for Gyro functions
#*
#* - - - - - - - - - License information: - - - - - - - - -
#*
#*  Copyright (C) 2011 and beyond by Yoctopuce Sarl, Switzerland.
#*
#*  Yoctopuce Sarl (hereafter Licensor) grants to you a perpetual
#*  non-exclusive license to use, modify, copy and integrate this
#*  file into your software for the sole purpose of interfacing
#*  with Yoctopuce products.
#*
#*  You may reproduce and distribute copies of this file in
#*  source or object form, as long as the sole purpose of this
#*  code is to interface with Yoctopuce products. You must retain
#*  this notice in the distributed source file.
#*
#*  You should refer to Yoctopuce General Terms and Conditions
#*  for additional information regarding your rights and
#*  obligations.
#*
#*  THE SOFTWARE AND DOCUMENTATION ARE PROVIDED 'AS IS' WITHOUT
#*  WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING
#*  WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY, FITNESS
#*  FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO
#*  EVENT SHALL LICENSOR BE LIABLE FOR ANY INCIDENTAL, SPECIAL,
#*  INDIRECT OR CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA,
#*  COST OF PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY OR
#*  SERVICES, ANY CLAIMS BY THIRD PARTIES (INCLUDING BUT NOT
#*  LIMITED TO ANY DEFENSE THEREOF), ANY CLAIMS FOR INDEMNITY OR
#*  CONTRIBUTION, OR OTHER SIMILAR COSTS, WHETHER ASSERTED ON THE
#*  BASIS OF CONTRACT, TORT (INCLUDING NEGLIGENCE), BREACH OF
#*  WARRANTY, OR OTHERWISE.
#*
#*********************************************************************/

import math

#####################################################################

# takes the 4 quaternion outputs of the INU gyro and produces meaningful
# roll, pitch an heading (i.e. compass) angles

def gyro_to_angles(orientation_x, orientation_y, orientation_z, orientation_w):

    # code section lifted from lines 386 - 404 of yocto_gyro.py example
    # provided with YoctoLib.python 28878 (November 2017)

    # ----

    sqw = orientation_w * orientation_w;
    sqx = orientation_x * orientation_x;
    sqy = orientation_y * orientation_y;
    sqz = orientation_z * orientation_z;
    norm = sqx + sqy + sqz + sqw;
    delta = orientation_y * orientation_w - orientation_x * orientation_z;

    if delta > 0.499 * norm:
            # // singularity at north pole
            roll = 0; # added - T. Breckon (this is a fudge, not correct) **
            pitch = 90.0;
            heading  = round(2.0 * 1800.0/math.pi * math.atan2(orientation_x,-orientation_w)) / 10.0;
    else:
            if delta < -0.499 * norm:
                # // singularity at south pole
                roll = 0; # added - T. Breckon (this is a fudge, not correct) **
                pitch = -90.0;
                heading  = round(-2.0 * 1800.0/math.pi * math.atan2(orientation_x,-orientation_w)) / 10.0;
            else:
                roll  = round(1800.0/math.pi * math.atan2(2.0 * (orientation_w * orientation_x +orientation_y * orientation_z),sqw - sqx - sqy + sqz)) / 10.0;
                pitch = round(1800.0/math.pi * math.asin(2.0 * delta / norm)) / 10.0;
                heading  = round(1800.0/math.pi * math.atan2(2.0 * (orientation_x * orientation_y + orientation_z * orientation_w),sqw + sqx - sqy - sqz)) / 10.0;

    # ----

    # ** - within the above code we will assume we are not operating at the North or South Pole
    # and if we are then the roll angle value here will be wrong and we'll have to just cope

    return roll, pitch, heading;

#####################################################################
