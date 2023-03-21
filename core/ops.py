import typing
from os import environ

import tweepy
from flask import send_file, request

from .exceptions import YoutubeVideoNotAvailable, TwitterVideoNotAvailable, InstagramVideoNotAvailable, TiktokVideoNotAvailable
from .parsers import Parsers

p = Parsers()


class Downloader:
    def __init__(self, twitter_bearer: str = None):
        """
        Initialize the Downloader class
        Twitter Bearer Token is required for the Twitter Downloader
        Twitter Bearer token can be obtained from https://developer.twitter.com/en/portal/dashboard


        Args:
            twitter_bearer:
        """
        self.token = twitter_bearer or environ.get('twitter_bearer')
        self.api = tweepy.Client(self.token)

    @staticmethod
    def youtube_downloader(identifier: str, quality: str = None, extension: str = None) -> send_file:
        """
        Download a video from YouTube
        Args:
            identifier: str
            quality: str
            extension:

        Returns:
            send_file
        """
        try:
            file, meta = p.get_youtube_video_by_id(identifier, quality=quality, extension=extension)
            return send_file(file, download_name=f"youtube-{meta['title']}.{extension or 'mp4'}", as_attachment=True)
        except Exception as e:
            raise YoutubeVideoNotAvailable('The video you are trying to download is not available')

    def twitter_downloader(self, identifier: str, quality: str = None, extension: str = None) -> send_file:
        """
        Download a video from twitter
        Args:
            extension: str
            quality: str
            identifier: str

        Returns:
            send_file
        """
        try:
            print(request.data)
            file, tweet = p.get_twitter_video_by_id(self.api, identifier)
            return send_file(file, download_name=f"twitter-{tweet.includes['users'][0]['username']}-{identifier}.mp4", as_attachment=True)
        except Exception as e:
            raise TwitterVideoNotAvailable('Twitter video is not available. Please check the identifier and try again. If the problem persists, please contact the developer.')

    def instagram_downloader(self, identifier: str = '', type: str = typing.Union['reels', 'p'], quality: str = None, extension: str = None) -> send_file:
        """
        Download a video from instagram
        Args:
            type: str (reels or p)
            identifier: str
            quality: str
            extension:

        Returns:
            send_file
        """
        try:
            file = p.get_instagram_video_by_id(identifier)
            return send_file(file, download_name=f'instagram-{type}-{identifier}.mp4', as_attachment=True)
        except Exception as e:
            raise InstagramVideoNotAvailable('Instagram video is not available. Please check the identifier and try again. If the problem persists, please contact the developer.')

    def tiktok_downloader(self, identifier: int) -> send_file:
        """
        Download a video from tiktok
        Args:
            identifier:

        Returns:

        """
        try:
            file = p.get_tiktok_video_by_id(identifier)
            return send_file(file, download_name=f'tiktok-{identifier}.mp4', as_attachment=True)
        except Exception as e:
            print(e)
            raise TiktokVideoNotAvailable('Tiktok video is not available. Please check the identifier and try again. If the problem persists, please contact the developer.')
