import re
from io import BytesIO
from os import environ
import tweepy
import wget
import yt_dlp
from flask import send_file



class Downloader:
    def __init__(self):
        token = environ.get('twitter_bearer')
        self.api = tweepy.Client(token)

    @staticmethod
    def youtube_downloader(identifier: str, quality=None, extension=None):
        """
        Download a video from youtube

        :param identifier:
        :param quality:
        :param extension:
        :return:
        """
        if "youtube.com" in identifier or "youtu.be" in identifier:
            # Extract the video ID from the URL
            identifier = re.findall(r"(?:v=|be/)([\w-]+)", identifier)[0]
        url = f"https://www.youtube.com/watch?v={identifier}"
        ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 'outtmpl': 'downloads/youtube/%(id)s.%(ext)s', 'ffmpeg_location': 'ffmpeg/bin/ffmpeg.exe'}

        if quality:
            ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'

        if extension:
            ydl_opts['format'] = f'bestaudio/best' if extension == 'mp3' else f'bestvideo[ext={extension}]+bestaudio[ext={extension}]/best[ext={extension}]'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if extension == 'mp3' else []

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            url = f"https://www.youtube.com/watch?v={identifier}"
            info_dict = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(info_dict)
            file = BytesIO()
            ydl.process_info(info_dict)
            with open(filename, 'rb') as f:
                file.write(f.read())
            file.seek(0)

            return send_file(file, download_name=f"{info_dict['title']}.{extension or 'mp4'}", as_attachment=True)

    def twitter_downloader(self, identifier: str):
        """
        Download a video from twitter
        :param identifier:
        :return:
        """
        video_url = ''
        tweet = self.api.get_tweet(identifier,
                                   expansions=['attachments.media_keys', 'author_id'],
                                   tweet_fields=['created_at', 'text', 'id', 'attachments', 'author_id', 'entities'],
                                   media_fields=['url', 'duration_ms', 'height', 'width', 'preview_image_url', 'type', 'variants'],
                                   user_fields=['username']
                                   )
        print(f"Tweet: {str(tweet).encode('utf-8')}")
        print(f"Tweet Includes: {str(tweet.includes).encode('utf-8')}")
        print(f"Tweet Meta: {str(tweet.meta).encode('utf-8')}")
        for variant in tweet.includes['media'][0]['variants']:
            print(variant)
            if variant['content_type'] == 'video/mp4':
                video_url = variant['url']
                break
        print(video_url)
        wget.download(video_url, out=f"downloads/twitter/{tweet.includes['users'][0]['username']}-{identifier}.mp4")
        file = BytesIO()
        with open(f"downloads/twitter/{tweet.includes['users'][0]['username']}-{identifier}.mp4", 'rb') as f:
            file.write(f.read())
        file.seek(0)
        return send_file(file, download_name=f"{tweet.includes['users'][0]['username']}-{identifier}.mp4", as_attachment=True)
