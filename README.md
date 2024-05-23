## @wifiovermybody Script Collection

![Convert](https://github.com/wifiovermybody/dynamic-frames-to-video/blob/main/convert.png)
![Clair](https://github.com/wifiovermybody/dynamic-frames-to-video/blob/main/clair.gif)
![Convert2](https://github.com/wifiovermybody/dynamic-frames-to-video/blob/main/convert2.png)
## Dynamic Frames to Video

* At the core very basic frame to video script.
* Converts a series of image frames into video files. It outputs two video formats: H.264 (.mp4) and ProRes (.mov). The user can specify either the desired frame rate (frames per second) or the total duration (in seconds) for the resulting video.

## Notes 
* It shouldn't matter how your image sequences is named. Eg. 0000001.png, frame_0002.png, etc AND it does not matter if your file does not start at 0 or 1. eg. 00053.png is the first frame. <br/>
* This script also has the ability to compile your frames into a specifc duration video. Ie. If there are 1200 frames, and you input 3 seconds on launch - it will compile all 1200 frames into the 3 second video file. <br/>
* This script should help automate the process of converting a sequence of image frames into video files with user-defined frame rate or duration, making it a useful tool for various video processing tasks.

## Prerequisites

- **ffmpeg-python**: Install the `ffmpeg-python` library:

  ```bash

  pip install ffmpeg-python

## Running the Script

1. Prepare Your Frames Directory: Ensure you have a directory containing your image frames. The frames should follow a sequential naming convention like frame_0001.png, frame_0002.png, or 00000007.png, 00000008.png, etc.

2. Open your terminal, type python3 (include space) and drag your frames_to_video.py into the terminal which will paste the path name, then paste the pathname of where your sequentional PNG sequence is location 

  ```bash

python3 /path/to/file/frames_to_video.py <path_to_frames_directory>
```

For example:

  ```bash
python3 /Users/Kynan/Scripts/frames_to_video.py /Users/Kynan/output_frames

```


## What the Script Does

1. Validates Input Directory: Checks if the specified frames directory exists.
2. Determines Frame Pattern: Identifies the naming pattern of the image frames, the starting frame number, and the total number of frames.
3. Prompts for User Input: Asks the user to enter either the desired frame rate (e.g., 30 for 30 fps) or the total duration (e.g., 5s for 5 seconds).
4. Calculates Frame Rate if Duration is Given: If a duration is provided, it calculates the frame rate required to fit all frames into the specified duration.
5. Creates Output Directory: Creates a subdirectory named video inside the frames directory to store the resulting video files.
6. Generates Videos: Uses ffmpeg to create two video files:
7. H.264 encoded video (.mp4)
8. ProRes encoded video (.mov)



