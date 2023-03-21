import asyncio
import random
from io import BytesIO

import requests
import wget
import yt_dlp
from TikTokApi import TikTokApi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Parsers:
    @staticmethod
    def get_tiktok_video_by_id(identifier):
        """
        Get tiktok video by id
        Args:
            identifier:

        Returns:

        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        did = str(random.randint(10000, 999999999))
        with TikTokApi(custom_verify_fp='verify_lfdrm2pt_gkaIEDYl_YlCW_4S2V_9eUs_aVmH7AsGslUx', custom_device_id=did, use_test_endpoints=True) as api:
            video = api.video(id=identifier)
            video_data = video.bytes()
            file = BytesIO(video_data)
            file.seek(0)
            return file

    @staticmethod
    def get_instagram_video_by_id(identifier):
        """
        Get instagram video by id
        Args:
            identifier:

        Returns:

        """
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        post_url = f'https://www.instagram.com/'
        if type == 'reels':
            driver.get(post_url + f'reel/{identifier}/')
        elif type == 'p':
            driver.get(post_url + f'p/{identifier}/')
        else:
            raise ValueError('Invalid type. Type must be either "reels" or "p"')
        wait = WebDriverWait(driver, 20)
        video_element = wait.until(EC.presence_of_element_located((By.XPATH, '//video[@playsinline and @preload="none"]')))
        video_url = video_element.get_attribute('src')

        driver.quit()
        response = requests.get(video_url)
        file = BytesIO(response.content)
        file.seek(0)
        return file

    @staticmethod
    def get_twitter_video_by_id(api, identifier):
        """
        Get twitter video by id
        Args:
            api:
            identifier:

        Returns:

        """
        video_url = ''
        tweet = api.get_tweet(identifier,
                              expansions=['attachments.media_keys', 'author_id'],
                              tweet_fields=['created_at', 'text', 'id', 'attachments', 'author_id', 'entities'],
                              media_fields=['url', 'duration_ms', 'height', 'width', 'preview_image_url', 'type', 'variants'],
                              user_fields=['username']
                              )
        for variant in tweet.includes['media'][0]['variants']:
            if variant['content_type'] == 'video/mp4':
                video_url = variant['url']
                break
        wget.download(video_url, out=f"downloads/twitter/{tweet.includes['users'][0]['username']}-{identifier}.mp4")
        file = BytesIO()
        with open(f"downloads/twitter/{tweet.includes['users'][0]['username']}-{identifier}.mp4", 'rb') as f:
            file.write(f.read())
        file.seek(0)
        return file, tweet

    @staticmethod
    def get_youtube_video_by_id(identifier, quality: str = None, extension: str = None):
        """
        Get youtube video by id
        Args:
            identifier:
            quality:
            extension:

        Returns:

        """
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
            return file, info_dict
