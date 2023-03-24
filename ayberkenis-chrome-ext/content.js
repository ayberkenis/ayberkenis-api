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