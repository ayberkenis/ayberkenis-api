# AyberkEnis API

#### AyberkEnis API is a free and open source API that allows you to download videos from YouTube, Twitter, Instagram, and TikTok. 

As mentioned above, this API is free and open source. You can use it for free and you can also contribute to the project. If you want to contribute, you can fork the project and make a pull request. If you want to use the API, you can use the API endpoint below.

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


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
