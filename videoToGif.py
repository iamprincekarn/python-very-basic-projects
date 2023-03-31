from moviepy.editor import VideoFileClip

def convert_to_gif(input_file, output_file):
    # Load the video clip
    clip = VideoFileClip(input_file)

    # Set the frames per second of the GIF to 15
    fps = 15

    # Get the duration of the clip and create a subclip with the same duration
    subclip = clip.subclip(30, 32)

    # Write the GIF file
    subclip.write_gif(output_file, fps)

    # Close the video clip
    clip.close()

# Example usage
input_file = "test.mp4"
output_file = "gifFile.gif"
convert_to_gif(input_file, output_file)
