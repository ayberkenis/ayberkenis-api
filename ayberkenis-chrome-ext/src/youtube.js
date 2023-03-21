var youtubeDownloader = function () {
    console.log('[1] init fire');

    function checkIfUserIsOnYoutubeWebsite() {
        return -1 != document.location.href.indexOf('youtube.com/') || -1 != document.location.href.indexOf('youtube.com/');
    }

    function downloadVideo(statusId, elem) {
        elem.html('<i class="fa-solid fa-download"></i> Downloading...');
        chrome.runtime.sendMessage({id: statusId, source: 'youtube'}, function (response) {
            if (response.message == 'Download finished') {
                console.log('Download finished');
                elem.html('<i class="fa-solid fa-download"></i> Download');
            } else {
                console.log('Download error');
                elem.html('<i class="fa-solid fa-download"></i> Download');
            }
        });
    }

    function downloadShortsVideo(statusId, elem) {
        elem.parent().addClass('ae-youtube-shorts-downloading');
        chrome.runtime.sendMessage({id: statusId, source: 'youtube'}, function (response) {
            if (response.message == 'Download finished') {
                console.log('Download finished');
                elem.parent().removeClass('ae-youtube-shorts-downloading');
            } else {
                console.log('Download error');
                elem.parent().removeClass('ae-youtube-shorts-downloading');
            }
        });
    }

    function insertDownloadLink(container) {
        console.log('[2] trying to find element...');
        const videoActionsContainer = container;


        const statusId = document.location.href.split('=')[1];
        console.log(statusId);

        var downloadLink = $('<div class="ae-youtube-div"><a class="ae-youtube-downloader" title="Download"><i class="fa-solid fa-download"></i> Download</a></div>');
        downloadLink.find('a.ae-youtube-downloader').click(function () {
            $(this).html('<i class="fa-solid fa-download"></i> Downloading...</a>');
            downloadVideo(statusId, $(this));
        });
        videoActionsContainer.after(downloadLink);
        videoActionsContainer.attr('mark', 1);
    }

    function insertDownloadLinkShorts(container) {
        console.log('[2] trying to find SHORTS element...');
        const videoActionsContainer = container;

        const statusId = document.location.href.split('/shorts/')[1];
        console.log(statusId);

        var downloadLink = $('<div class="ae-youtube-shorts-div"><a class="ae-youtube-shorts-downloader" title="Download"><i class="fa-solid fa-download"></i></a></div>');
        downloadLink.find('a.ae-youtube-shorts-downloader').click(function () {
            $(this).parent().addClass('ae-youtube-shorts-downloading');
            downloadShortsVideo(statusId, $(this));
        });

        videoActionsContainer.after(downloadLink);
        videoActionsContainer.attr('mark', 1);
    }

function checkForDOMNodeToAppear() {
    const targetNode = $('body')[0];

    const checkForButtons = function() {
        const videoActionsContainer = $('.style-scope.ytd-menu-renderer[button-renderer=true]');
        const shortsButtonsContainer = $('div.button-container.style-scope.ytd-reel-player-overlay-renderer:nth-of-type(4)').after();

        if (videoActionsContainer.length && !videoActionsContainer.attr('mark')) {
            insertDownloadLink(videoActionsContainer);
        }
        if (shortsButtonsContainer.length && !shortsButtonsContainer.attr('mark')) {
            insertDownloadLinkShorts(shortsButtonsContainer);
        }
    };

    // Check for buttons every 2 seconds
    const intervalId = setInterval(checkForButtons, 200);

    // Disconnect observer after 30 seconds
    setTimeout(function() {
        clearInterval(intervalId);
    }, 30000);
}


    let q;

    (function (s) {
        var u = document.createElement('a');
        return u.href = s, u;
    })(document.location.href);

    $(function () {
        checkForDOMNodeToAppear();
    });
}();
