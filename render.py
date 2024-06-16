from IPython.display import Video, display
import moviepy.editor as mpy


def show_video(frames):
    clip = mpy.ImageSequenceClip(frames, fps=30)
    file_path = './render_videos/tmp.mp4'
    clip.write_videofile(file_path, codec='libx264')
    display(Video(file_path, embed=True))
