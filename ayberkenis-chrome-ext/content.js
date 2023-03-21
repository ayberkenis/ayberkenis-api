var SaveTweetVid = function () {
    console.log('[1] init fire');

    function checkIfUserIsOnTwitterWebsite() {
        return -1 != document.location.href.indexOf('twitter.com/') || -1 != document.location.href.indexOf('twitter.com/');
    }

    function downloadVideo(statusId) {
        chrome.runtime.sendMessage({videoUrl: statusId}, function (response) {
            console.log(response);
        });
    }

    function insertDownloadLink() {
        console.log('[2] trying to find element...');

        // New twitter
        if ($('article[role=article]').length) {
            console.log('new twitter')
            $('article[role=article][mark!=1]').each(function () {
                var tweetContainer = $(this),
                    hasVideo = tweetContainer.find('video');

                console.log('[3] video element detect try... ' + hasVideo.length);

                if (hasVideo.length) {
                    console.log('[3] video element found!');

                    // Is it a single tweet? If so, status ID can be taken from URI
                    var statusId = document.location.href.split('/status/')[1];

                    // It is a list of tweets, status ID is taken from link with certain class
                    if (!statusId) {
                        var linkFromTweetsList = tweetContainer.find('a.r-3s2u2q[role=link]');
                        statusId = linkFromTweetsList.attr('href').split('/status/')[1];
                    }

                    console.log('[4] status ID found: ' + statusId);

                    var downloadLink = $('<div class="ae-twitter-div css-1dbjc4n r-18u37iz r-1h0z5md"><a class="ae-twitter-downloader" title="Download"><i class="fa-solid fa-download r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi"></i></a></div>');
                    downloadLink.find('a.ae-twitter-downloader').click(function () {
                        downloadVideo(statusId);
                    });
                    var A = tweetContainer.find('.css-1dbjc4n.r-18u37iz.r-1h0z5md:nth-last-child(2)');
                    console.log(A);
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
