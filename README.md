# Stereo Vision Disparity Tools

a small selection of tools for calculating disparity and working with the rectified output from the CR MultiSense S21 stereo camera (and optional Yoctopuce GPS/IMU data if available)

OpenCV Python computer vision examples used for teaching and research within the undergraduate Computer Science programme
at [Durham University](http://www.durham.ac.uk) (UK) by [Prof. Toby Breckon](http://community.dur.ac.uk/toby.breckon/).

All tested with [OpenCV](http://www.opencv.org) 3.x and Python 3.x.

---

### Tools

- *stereo_disparity.py* – cycles through the dataset and calculates the disparity from the left and right stereo images provided.
- *stereo_to_3d.py* – projects a single example stereo pair to a 3D, write a point cloud of this data to an ASCII X Y Z file for reference (which can be viewed via
this [online tool](http://lidarview.com/), another 3D point cloud viewer (e.g. [http://www.pointcloudviz.com/](http://www.pointcloudviz.com/)) or using the [open3d](http://www.open3d.org/) library) and shows an example back-projection from 3D to the 2D image.
- *planar_fitting_hints.py* – a set of hints (aimed at Durham L3 2017/18 students) on how to efficiently use some of the advanced library features of Python to compute the coefficients of a plane from a given set of 3D points.
- *mono_stream.py* –  cycles through the _left or right only_ image only from the dataset and displays GPS / IMU data if available (aimed at Durham L4 2017/18 students).
- *gyro.py* - supporting function for mono_stream.py that converts IMU gyroscope readings to roll/pitch/heading angles when this data is available
- *correlate.py* - cycle through a set of images from a directory and prints file names of images that strongly correlate with the one before it (i.e. not much, if anything has changed)
---

### How to download and run:

Download each file as needed or to download the entire repository and run each try:

```
git clone https://github.com/tobybreckon/stereo-disparity.git
cd stereo-disparity

< edit example with your favourite editor to set path to your rectified stereo data

python3 ./<insert file name of one of the examples.py>
```
---

### Data Set Background

Internal data sets that these tools are known to work with:

- To The Bailey & Back (TTBB), Durham, 02-10-17 subsampling at 10 (TTBB-durham-02-10-17-sub10)
- To The Bailey & Back (TTBB), Durham, 02-10-17 subsampling at 5 (TTBB-durham-02-10-17-sub5)

Originally recorded onboard via [ROS](http://www.ros.org) as the following topics:

```
/clock
/multisense/left/image_rect_color
/multisense/right/image_rect
/yoctopuce/fix
/yoctopuce/imu
```

---

### References

The settings and approaches used in the above examples where informed and inspired by the following research work:

- [Generalized Dynamic Object Removal for Dense Stereo Vision Based Scene Mapping using Synthesised Optical Flow](http://community.dur.ac.uk/toby.breckon/publications/papers/hamilton16removal.pdf) (O.K. Hamilton, T.P. Breckon), In Proc. International Conference on Image Processing, IEEE, pp. 3439-3443, 2016. [[pdf](http://community.dur.ac.uk/toby.breckon/publications/papers/hamilton16removal.pdf)] [[doi](http://dx.doi.org/10.1109/ICIP.2016.7532998)]

- [Quantitative Evaluation of Stereo Visual Odometry for Autonomous Vessel Localisation in Inland Waterway Sensing Applications](http://community.dur.ac.uk/toby.breckon/publications/papers/kriechbaumer15vessel.pdf) (T. Kriechbaumer, K. Blackburn, T.P. Breckon, O. Hamilton, M. Riva-Casado), In Sensors, MDPI, Volume 15, No. 12, pp. 31869-31887, 2015. [[pdf](http://community.dur.ac.uk/toby.breckon/publications/papers/kriechbaumer15vessel.pdf)] [[doi](http://dx.doi.org/10.3390/s151229892)]

- [A Foreground Object based Quantitative Assessment of Dense Stereo Approaches for use in Automotive Environments](http://community.dur.ac.uk/toby.breckon/publications/papers/hamilton13stereo.pdf) (O.K. Hamilton, T.P. Breckon, X. Bai, S. Kamata), In Proc. International Conference on Image Processing, IEEE, pp. 418-422, 2013.[[pdf](http://community.dur.ac.uk/toby.breckon/publications/papers/hamilton13stereo.pdf)] [[doi](http://dx.doi.org/10.1109/ICIP.2013.6738086)]

- [An Empirical Comparison of Real-time Dense Stereo Approaches for use in the Automotive Environment](http://community.dur.ac.uk/toby.breckon/publications/papers/mroz12stereo.pdf) (F. Mroz, T.P. Breckon), In EURASIP Journal on Image and Video Processing, Springe, Volume 2012, No. 13, pp. 1-19, 2012. [[demo](http://community.dur.ac.uk/toby.breckon/demos/autostereo/)] [[pdf](http://community.dur.ac.uk/toby.breckon/publications/papers/mroz12stereo.pdf)] [[doi](http://dx.doi.org/10.1186/1687-5281-2012-13)]

---

If you find any bugs raise an issue (or much better still submit a git pull request with a fix) - toby.breckon@durham.ac.uk

_"may the source be with you"_ - anon.
