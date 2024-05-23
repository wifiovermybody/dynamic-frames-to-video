import ffmpeg
import os
import sys
import re

def get_user_input(prompt):
    """
    Get user input for frame rate or duration.

    :param prompt: The prompt message.
    :return: Frame rate (in frames per second) or duration (in seconds).
    """
    while True:
        user_input = input(prompt)
        if user_input.endswith('s'):
            try:
                duration = float(user_input[:-1])
                return 'duration', duration
            except ValueError:
                print("Invalid input. Please enter a valid number followed by 's' for seconds.")
        else:
            try:
                frame_rate = float(user_input)
                return 'frame_rate', frame_rate
            except ValueError:
                print("Invalid input. Please enter a valid number for frame rate.")

def get_frame_pattern(frames_dir):
    """
    Determine the frame file pattern and the starting frame number based on the files in the directory.

    :param frames_dir: Path to the directory containing frames.
    :return: A tuple with the frame file pattern, the common prefix, the starting frame number, and the total number of frames.
    """
    files = sorted(os.listdir(frames_dir))
    pattern = re.compile(r'(\D*)(\d+)(\D*)\.png')
    frame_files = [file for file in files if pattern.match(file)]
    if frame_files:
        match = pattern.match(frame_files[0])
        prefix, num, suffix = match.groups()
        start_number = int(num)
        total_frames = len(frame_files)
        return f'{prefix}%0{len(num)}d{suffix}.png', prefix + suffix, start_number, total_frames
    return None, None, None, 0

def convert_frames_to_video(frames_dir):
    """
    Convert frames to video files.

    :param frames_dir: Path to the directory containing frames.
    """
    if not os.path.exists(frames_dir):
        print(f"Error: The frames directory '{frames_dir}' does not exist.")
        sys.exit(1)

    # Get frame file pattern
    input_pattern, common_prefix, start_number, total_frames = get_frame_pattern(frames_dir)
    if not input_pattern:
        print(f"Error: No frames found in the directory '{frames_dir}'.")
        sys.exit(1)

    print(f"Using input pattern: {input_pattern} starting at frame {start_number} with total frames {total_frames}")

    # Define the video subdirectory path
    video_dir = os.path.join(frames_dir, 'video')
    os.makedirs(video_dir, exist_ok=True)

    # Get the base name of the frames directory
    frames_base_name = os.path.basename(frames_dir)

    # Define output video paths
    h264_output_path = os.path.join(video_dir, f'{frames_base_name}_h264.mp4')
    prores_output_path = os.path.join(video_dir, f'{frames_base_name}_prores.mov')

    # Get user input for frame rate or duration
    input_type, value = get_user_input("Enter the desired frame rate (fps) or duration (seconds with 's' after the number): ")

    input_pattern = os.path.join(frames_dir, input_pattern)

    if input_type == 'duration':
        # Calculate the required frame rate to fit all frames into the desired duration
        frame_rate = total_frames / value
    else:
        frame_rate = value

    # Use ffmpeg to convert frames to videos
    try:
        (
            ffmpeg
            .input(input_pattern, framerate=frame_rate, start_number=start_number)
            .output(h264_output_path, vcodec='libx264', pix_fmt='yuv420p')
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"H.264 video saved to '{h264_output_path}' successfully.")

        (
            ffmpeg
            .input(input_pattern, framerate=frame_rate, start_number=start_number)
            .output(prores_output_path, vcodec='prores_ks')
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"ProRes video saved to '{prores_output_path}' successfully.")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode('utf8')}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_frames_directory>")
        sys.exit(1)

    frames_dir = sys.argv[1]
    convert_frames_to_video(frames_dir)
