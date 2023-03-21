var SaveTweetVid = function () {
    function checkIfUserIsOnTwitterWebsite() {
        return -1 != document.location.href.indexOf('twitter.com/') || -1 != document.location.href.indexOf('twitter.com/');
    }

    function downloadVideo(statusId, elem) {
        console.log('Download started');
        elem.html('<i class="fa-solid fa-download"></i> Downloading...');
        chrome.runtime.sendMessage({id: statusId, source: 'twitter'}, function (response) {
            console.log(response)
            if (response.message == 'Download finished') {
                console.log('Download finished');
                elem.html('<i class="fa-solid fa-download"></i> Download Video');
            } else if (response.message == 'Download failed') {
                console.log('Download failed');
                elem.html('<i class="fa-solid fa-download"></i> Download Video');
            } else {
                console.log('Download error');
                elem.html('<i class="fa-solid fa-download"></i> Download Video');
            }
        });
    }

    function insertDownloadLink() {

        // New twitter
        if ($('article[role=article]').length) {
            $('article[role=article][mark!=1]').each(function () {
                var tweetContainer = $(this),
                    hasVideo = tweetContainer.find('video');

                if (hasVideo.length) {


                    // Is it a single tweet? If so, status ID can be taken from URI
                    var statusId = document.location.href.split('/status/')[1];

                    // It is a list of tweets, status ID is taken from link with certain class
                    if (!statusId) {
                        var linkFromTweetsList = tweetContainer.find('a.r-3s2u2q[role=link]');
                        statusId = linkFromTweetsList.attr('href').split('/status/')[1];
                    }


                    var downloadLink = $('<div class="ae-twitter-div css-1dbjc4n r-18u37iz r-1h0z5md"><a class="ae-twitter-downloader" title="Download"><i class="fa-solid fa-download r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi"></i> Download Video</a></div>');
                    downloadLink.find('a.ae-twitter-downloader').click(function () {
                        downloadVideo(statusId, $(this));
                    });
                    var A = tweetContainer.find('.css-1dbjc4n.r-18u37iz.r-1h0z5md:nth-last-child(2)');
                    A.before(downloadLink); // Inserts the link after ^ container with such class
                    tweetContainer.attr('mark', 1); // Check as marked only after download link was added
                }
            });
        }
    }

    function checkForDOMNodeToAppear() {
        chrome.storage.local.get('checker', function (s) {
            void 0 == s.checker && (s.checker = !0, chrome.storage.local.set({
                checker: !0
            })), checkIfUserIsOnTwitterWebsite() && s.checker && ($(document).bind('DOMNodeInserted', function () {
                clearTimeout(q), q = setTimeout(function () {
                    insertDownloadLink();
                }, 200);
            }), insertDownloadLink());
        });
    }

    var q;

    (function (s) {
        var u = document.createElement('a');
        return u.href = s, u;
    })(document.location.href);

    $(function () {
        checkForDOMNodeToAppear();
    });
}();
