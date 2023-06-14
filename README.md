### Segmentation using ImageJ macros

* Do this one time only: 
    1. Download [miniconda](https://docs.conda.io/en/latest/miniconda.html) if you haven't already.
        * Follow installation instructions online. **ACCEPT THE DEFAULTS WHEN PROMPTED.** [Email Eeshaan](mailto:er479@cornell.edu) with any questions.
            * If you are on an M1/M2 Mac, download this: [https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh). Then, enter in your terminal `bash Miniconda3-latest-MacOSX-arm64.sh`.
            * If you are on an older Intel Mac, download this: [https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh). Then, enter in your terminal `bash Miniconda3-latest-MacOSX-arm64.sh`.
            * If you are on a Windows computer, download this: [https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe). Double-click the installed file (...exe) and follow the on-screen instructions. I'm not 100% on how the install and future steps work with Windows so please email me so we can meet and get it set up.  
        * Test it with `conda`.
    2. Download [git repository](https://github.com/eeshaanrehani/imageJ-tracing) using one of the following methods:
        * Using git: `git clone git@github.com:eeshaanrehani/fb-follicle-seg.git`
        * By downloading zip file of code: `wget "https://github.com/eeshaanrehani/fb-follicle-seg/archive/refs/heads/main.zip"`
        * By [downloading directly](https://github.com/eeshaanrehani/imageJ-tracing/archive/refs/heads/main.zip).
    3. Set up conda environment.
        * `conda env create -f environment.yml`
        * If prompted `[y/n]`: `y`.


