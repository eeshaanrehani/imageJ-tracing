// Macro to select an image, create ROIs, and save a binary mask
// Eeshaan Rehani - eer4001@med.cornell.edu

// Select a directory
dir = getDirectory("Select a Directory");

// Get list of files in the directory
list = getFileList(dir);

if (list.length < 1) {
	exit("No files in selected directory");
}

for (i = 0; i < list.length; i++) {
	fileName = list[i];

	// Check if the file ends with "_original.tiff"
	if (endsWith(fileName, "_original.tiff")) {
		// Open the image
		open(dir + fileName);

		// Run the segmentation editor
		run("Segmentation Editor");

		// Change the mask color to white
		run("8-bit");

		// Save the annotated mask with "_follicle.tiff" suffix
		newFileName = replace(fileName, "_original.tiff", "_ovary.tiff");
		saveAs("Tiff", dir + newFileName);

		// Close the image
		close();
	}
}

print("Script completed.");

