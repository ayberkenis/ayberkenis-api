var InstagramDownloader = function () {
    console.log('InstagramDownloader');
    function getVideoId() {
        return document.URL.match(/\/p\/([^&]+)/)[1];
    }


    function insertDownloadLink(container, type) {
        let statusId = getVideoId();

        let wrapperClassName = 'ae-instagram-div';
        let downloaderClassName = 'ae-instagram-downloader';
        let downloadLink = $(`
<div class="${wrapperClassName}">
  <a class="${downloaderClassName}" title="Download">
    <i class="fa-solid fa-download"></i> Download
  </a>
</div>
`);

        container.parent().find(`.${wrapperClassName}`).remove();
        downloadLink.find(`a.${downloaderClassName}`).click(function () {
            downloadVideo(statusId, $(this), type);
        });

        container.after(downloadLink);
        localStorage.setItem('buttonInserted', 'true');

    }

    function downloadVideo(statusId, elem, type) {
        chrome.runtime.sendMessage({id: statusId, source: 'instagram'}, function (response) {
            if (response.message === 'Download finished') {
                console.log('Download finished');
                elem.html('<i class="fa-solid fa-download"></i> Download');
            } else {
                console.log('Download error');
                elem.html('<i class="fa-solid fa-download"></i> Download');
            }
        });
    }


    function checkDOMEveryInterval() {
        const interval = setInterval(function () {
            const currentURL = window.location.href;
            const storedURL = localStorage.getItem('currentURL');
            // Reset buttonInserted if the URL has changed
            if (currentURL !== storedURL) {
                localStorage.clear();
                localStorage.setItem('buttonInserted', 'false');
                localStorage.setItem('currentURL', currentURL);
            }
            if (localStorage.getItem('buttonInserted') === 'false') {
                console.log('[1] trying to find element...')
                console.log('buttonInserted: ', localStorage.getItem('buttonInserted'))
                const videoActionsContainer = $('section > span:last').after();
                if (videoActionsContainer.length) {
                    insertDownloadLink(videoActionsContainer, 'video');
                    localStorage.setItem('buttonInserted', 'true');
                }
            }
        }, 500);
    }

    checkDOMEveryInterval()

}

$(window).on('load', function () {
    localStorage.clear();
    localStorage.setItem('buttonInserted', 'false');
    InstagramDownloader();

    // Add event listener for URL changes
    window.addEventListener('hashchange', function () {
        localStorage.clear();
        localStorage.setItem('buttonInserted', 'false');
    });
});
