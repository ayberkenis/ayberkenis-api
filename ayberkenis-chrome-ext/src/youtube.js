var YouTubeDownloader = function () {

    function getVideoId() {
        // Get video ID from URL
        return document.URL.match(/v=([^&]+)/)[1];
    }

    function getShortsId() {
        // Get shorts ID from URL
        return document.URL.match(/shorts\/([^&]+)/)[1];
    }

    function insertDownloadLink(container, type) {
        // Insert download button, if it is not already inserted
        let statusId;
        let wrapperClassName;
        let downloaderClassName;
        let downloadLink;
        if (type === 'video') {
            statusId = getVideoId();
            wrapperClassName = 'ae-youtube-div';
            downloaderClassName = 'ae-youtube-downloader';
            downloadLink = $(`
<div class="${wrapperClassName}">
  <a class="${downloaderClassName}" title="Download">
    <i class="fa-solid fa-download"></i> Download
  </a>
</div>
`);

        } else if (type === 'shorts') {
            statusId = getShortsId();
            wrapperClassName = 'ae-youtube-shorts-div';
            downloaderClassName = 'ae-youtube-shorts-downloader';
            downloadLink = $(`
<div class="${wrapperClassName}">
    <a class="${downloaderClassName}" title="Download">
        <i class="fa-solid fa-download"></i>
    </a>
</div>
`);
        }

        container.parent().find(`.${wrapperClassName}`).remove();
        downloadLink.find(`a.${downloaderClassName}`).click(function () {
            downloadVideo(statusId, $(this), type);
        });

        container.after(downloadLink);
        localStorage.setItem('buttonInserted', 'true');

    }

    function downloadVideo(statusId, elem, type) {
        // Send message to background script to download video
        if (type === 'shorts') {
            elem.parent().addClass('ae-youtube-shorts-downloading');
        } else if (type === 'video') {
            elem.html('<i class="fa-solid fa-download"></i> Downloading...');
        }
        chrome.runtime.sendMessage({id: statusId, source: 'youtube'}, function (response) {

            if (response.message === 'Download finished') {
                console.log('Download finished');
                if (type === 'video') {
                    elem.html('<i class="fa-solid fa-download"></i> Download');
                } else if (type === 'shorts') {
                    elem.parent().removeClass('ae-youtube-shorts-downloading');
                }
            } else {
                console.log('Download error');
                if (type === 'video') {
                    elem.html('<i class="fa-solid fa-download"></i> Download');
                } else if (type === 'shorts') {
                    elem.parent().removeClass('ae-youtube-shorts-downloading');
                }
            }
        });
    }


    function checkDOMEveryInterval() {
        // Check if the DOM has elements every 500ms
        const interval = setInterval(function () {
            const currentURL = window.location.href;
            const storedURL = localStorage.getItem('currentURL');
            // Reset buttonInserted if the URL has changed
            if (currentURL !== storedURL) {
                localStorage.clear();
                localStorage.setItem('buttonInserted', 'false');
                localStorage.setItem('currentURL', currentURL);
            }
            if (localStorage.getItem('buttonInserted') === 'false' && currentURL.includes('watch?v=') || currentURL.includes('shorts/')) {
                // If the button is not inserted and the URL is a video or shorts URL
                // Find the container and insert the button
                // Set buttonInserted to true
                // We need to check for both video and shorts because the DOM is different
                // We also need to check if url contains watch?v= or shorts/ to avoid inserting buttons or calling unnecessary functions
                console.log('[1] trying to find element...')
                console.log('buttonInserted: ', localStorage.getItem('buttonInserted'))
                const videoActionsContainer = $('.style-scope.ytd-menu-renderer[button-renderer=true]:first');
                const shortsActionsContainer = $('div.button-container.style-scope.ytd-reel-player-overlay-renderer:nth-of-type(4)').after();
                if (videoActionsContainer.length) {
                    insertDownloadLink(videoActionsContainer, 'video');
                    localStorage.setItem('buttonInserted', 'true');
                }
                if (shortsActionsContainer.length) {
                    insertDownloadLink(shortsActionsContainer, 'shorts');
                    localStorage.setItem('buttonInserted', 'true');
                }

            }
        }, 500);
    }

    checkDOMEveryInterval()

}

$(window).on('load', function () {
    // Clear localStorage and set buttonInserted to false on page load
    localStorage.clear();
    localStorage.setItem('buttonInserted', 'false');
    YouTubeDownloader();

    // Add event listener for URL changes
    window.addEventListener('hashchange', function () {
        // As YouTube DOM is manipulated on certain events, we need to clear localStorage and set buttonInserted to false
        localStorage.clear();
        localStorage.setItem('buttonInserted', 'false');
    });
});
