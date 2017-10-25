# Stereo Vision Disparity Tools

a small selection of tools for calculating disparity and working with the rectified output from the CR MultiSense S21 stereo camera

OpenCV Python computer vision examples used for teaching and research within the undergraduate Computer Science programme
at [Durham University](http://www.durham.ac.uk) (UK) by [Prof. Toby Breckon](http://community.dur.ac.uk/toby.breckon/).

All tested with [OpenCV](http://www.opencv.org) 3.x and Python 3.x.

---

### Tools

- stereo_disparity.py – cycles through the dataset and calculates the disparity from the left and right stereo images provided.
- stereo_to_3d.py – projects a single example stereo pair to a 3D, write a point cloud of this data to an ASCII X Y Z file for reference (which can be viewed via
this [online tool](http://www.opencv.org) or another 3D point cloud viewer (e.g. [http://www.pointcloudviz.com/](http://www.pointcloudviz.com/))) and shows an example back-projection from 3D to the 2D image.
- planar_fitting_hints.py – a set of hints (aimed at Durham L3 2017/18 students) on how to efficiently use some of the advanced library features of Python to compute the coefficients of a plane from a given set of 3D points.

---

### How to download and run:

Download each file as needed or to download the entire repository and run each try:

```
git clone https://github.com/tobybreckon/stereo-disparity.git
cd stereo-disparity

< edit example with your favourite editor to set path to your rectified stereo data >

python3 ./<insert file name of one of the examples>.py
```

Internal data sets that these tools are known to work with:

- To The Bailey & Back (TTBB), Durham, 02-10-17 subsampling at 10 (TTBB-durham-02-10-17-sub10)

---

If you find any bugs raise an issue (or much better still submit a git pull request with a fix) - toby.breckon@durham.ac.uk

_"may the source be with you"_ - anon.
