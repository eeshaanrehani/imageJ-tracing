### Segmentation using ImageJ macros

**Do this one time only:**  
1. Download [miniconda](https://docs.conda.io/en/latest/miniconda.html) if you haven't already.
    * Follow installation instructions online. **ACCEPT THE DEFAULTS WHEN PROMPTED.** [Email Eeshaan](mailto:er479@cornell.edu) with any questions.
        * If you are on an M1/M2 Mac, download this: [https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh). Then, enter in your terminal `bash Miniconda3-latest-MacOSX-arm64.sh`.
        * If you are on an older Intel Mac, download this: [https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh). Then, enter in your terminal `bash Miniconda3-latest-MacOSX-arm64.sh`.
        * If you are on a Windows computer, download this: [https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe). Double-click the installed file (...exe) and follow the on-screen instructions. I'm not 100% on how the install and future steps work with Windows so please email me so we can meet and get it set up.  
    * Test it by going to your terminal and typing in: `conda`.
2. Download [git repository](https://github.com/eeshaanrehani/imageJ-tracing) using one of the following methods:
    * Using git: `git clone git@github.com:eeshaanrehani/imageJ-tracing.git`
    * By downloading zip file of code: `wget "https://github.com/eeshaanrehani/imageJ-tracing/archive/refs/heads/main.zip"`
    * By [downloading directly](https://github.com/eeshaanrehani/imageJ-tracing/archive/refs/heads/main.zip).
3. Enter the directory with the git repository: `cd /path/to/imageJ-tracing-main/`.
4. Set up conda environment.
    * `conda env create -f environment.yml`
    * If prompted `[y/n]`: `y`.

**Convert dicom stacks to .tif image slices:**
1. Type in your terminal: `conda activate dicom_imagej`.
2. Type in your terminal: `python dcm_to_tiff.py {DICOM_path} {save_directory}`. Replace `{DICOM_path}` and `{save_directory}` with the path to a DICOM file the directory you want masks and slices to be saved in. This command will convert the DICOM to tiff images for each individual slice, and save the slices as `.../{save_directory}/{DICOM_name}/{DICOM_name}_{slice}.tif`. It will also create another folder inside your save directory, `.../{save_directory}/mask_{DICOM_name}/`, which is where the masks will be saved. 

**Preparing the macro:**  
1. Open the terminal and go to the downloaded folder with the scripts in it: `cd /path/to/imageJ-tracing-main/`.
2. Open ImageJ, click `Plugins`>`Macros`>`Run`.
3. In the file explorer pop-up, select the script `DICOM_region_tracing.ijm` (this is in the folder `/imageJ-tracing-main/`).

**Using the macro:** _pay attention to the "log" window that imageJ creates_
1. In the first file explorer popup, select the DICOM you want to annotate.
2. In the next popup, select the folder you want to save slices and masks in. **Do not press 
    * This should theoretically be the same folder for every single DICOM - for each DICOM you select, the script will create two new folders inside: `/{DICOM_name}/`, and `/mask_{DICOM_name}`.
3. The log window will show the python commands from above. Ignore it if it's already been done.
4. In the dialog popup, enter the number of the first slice to annotate. Press OK.
5. Enter the number of the last slice to annotate. Press OK.
6. At this point, the screen will flash a lot as it opens and closes images. It is creating a blank mask for each slice up to the first one to annotate. When a new dialog box pops up, **do not press OK**.
7. Select the `freehand selections` tool in ImageJ (4th button from the left), and trace out the first item. In the ROI manager window, press `Add`, and then press `More`>`Fill`.
    * Repeat this for everything you want to segment in the slice.
8. When you are finished with a slice, press OK.
9. The next slice to annotate will pop up. Repeat steps 7-8. After the ending slice indicated earlier has been annotated, the screen will flash once again (as in step 6). It is creating a blank mask for each of the remaining slices. 
10. To start a new DICOM, see: **Preparing the macro**: Step 2.
