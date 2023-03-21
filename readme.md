# AyberkEnis API
![License](https://img.shields.io/github/license/ayberkenis/ayberkenis-api?style=flat-square)
![Discord](https://img.shields.io/discord/1029242783954894908?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/ayberkenis/ayberkenis-api?style=flat-square)
![Build](https://img.shields.io/github/checks-status/ayberkenis/ayberkenis-api/master?style=flat-square)
![API](https://img.shields.io/website?down_message=down&style=flat-square&up_message=up%20and%20running&url=https%3A%2F%2Fayberkenis.com.tr/api/v1/status)
![Issues](https://img.shields.io/github/issues/ayberkenis/ayberkenis-api?style=flat-square)
![PRs](https://img.shields.io/github/issues-pr/ayberkenis/ayberkenis-api?style=flat-square)

#### AyberkEnis API is a free and open source API that allows you to download videos from YouTube, Twitter, Instagram, and TikTok. 

As mentioned above, this API is free and open source. You can use it for free, and you can also contribute to the project. If you want to contribute, you can fork the project and make a pull request. If you want to use the API, you can use the API endpoint below.


#### Known Issues

Majority of the issues are related with the chrome extension. If you want to use the API, you can use the API endpoints below without extension. There shouldn't be any issues with the API itself.

- `Download Video` button might not appear on YouTube videos. This is a known issue, and it will be fixed soon. It has something to do with how YouTube renders the DOM.
- Even though API is down, Chrome extension still lets you download videos which is not intended.
- TikTok videos will be downloaded with watermark even though you select `noWatermark` option. This is a known issue but workaround is not available yet for TikTok's anti-scraping mechanism. So, It might take a while to fix this issue as it is not related with the repository.

#### Roadmap

- [x] YouTube Downloader
- [x] Twitter Downloader
- [x] Instagram Downloader
- [x] TikTok Downloader
- [ ] Add more downloaders (Facebook, Reddit, etc.)
- [ ] Options Page (Chrome Extension)
- [ ] Fix known issues
- [ ] Add more customizations for the Chrome Extension (Download location, etc.)
- [ ] Add more download options for the Chrome Extension (Download audio only, etc.)


## Base Endpoint
> ```http
> https://ayberkenis.com.tr/
> ```

> All parameters below needs to be sent in the request body. If you want to send a parameter in the url, you need to use the query string.
> For example, if you want to send a parameter named "extension" with the value "mp3", you need to send it like this: `?extension=mp3`
> But for better response, you should send it in the request body.

## Usage

### YouTube Downloader

```http GET
GET /api/v1/download/youtube/<identifier>
```

This API endpoint allows you to download YouTube videos by providing a video identifier, video format, and video quality.
Parameters are optional. If you don't provide any parameters, the API will download the video in the best quality and format.
Identifier is required on url path.

| Parameter  | Type   | Description                                             | Optional | 
|------------|--------|---------------------------------------------------------|:--------:|
| identifier | string | The Youtube video identifier to download.               |          | 
| extension  | string | mp4, webm, mkv, flv, ogg, mp3, wav, aac, m4a, best      |   [X]    |
| quality    | string | 144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p, best |   [X]    |

----

### Twitter Downloader

```http GET
GET /api/v1/download/twitter/<identifier>
```

| Parameter  | Type   | Description                                             | Optional | 
|------------|--------|---------------------------------------------------------|:--------:|
| identifier | string | The Twitter tweet status identifier                     |          | 
| extension  | string | mp4, webm, mkv, flv, ogg, mp3, wav, aac, m4a, best      |   [X]    |
| quality    | string | 144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p, best |   [X]    |

----

### Instagram Downloader

```http GET
GET /api/v1/download/instagram/<identifier>
```

| Parameter  | Type   | Description                                             | Optional |
|------------|--------|---------------------------------------------------------|:--------:|
| identifier | string | The Instagram post identifier                           |          |
| extension  | string | mp4, webm, mkv, flv, ogg, mp3, wav, aac, m4a, best      |   [X]    |
| quality    | string | 144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p, best |   [X]    |

----

### TikTok Downloader

```http GET
GET /api/v1/download/tiktok/<identifier>
```

| Parameter  | Type   | Description                                             | Optional |
|------------|--------|---------------------------------------------------------|:--------:|
| identifier | string | The TikTok video identifier                             |          |
| extension  | string | mp4, webm, mkv, flv, ogg, mp3, wav, aac, m4a, best      |   [X]    |
| quality    | string | 144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p, best |   [X]    |
| noWatermark| bool   | true, false                                             |   [X]    |


----

## Contributing

You can contribute to the project by forking the project and making a pull request. If you want to contribute, you can contact me on [Twitter](https://twitter.com/ayberkenis).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
