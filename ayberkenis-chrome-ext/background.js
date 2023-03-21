chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
    console.log('message received')
    console.log(message);


    let baseUrl = `http://127.0.0.1:5000/api/v1/downloader/${message.source}/`
    let url = baseUrl + message.id;
    const downloadOptions = {
        url: url,
        method: 'GET',
        saveAs: true,
        headers: [
            {name: 'Content-Type', value: 'application/json'}
        ]
    };

    chrome.downloads.download(downloadOptions, function(downloadId) {
        chrome.downloads.onChanged.addListener(function downloadListener(downloadDelta) {
            console.log(downloadDelta);
            if (downloadDelta.id === downloadId && downloadDelta.state) {
                if (downloadDelta.state.current === "complete") {
                    console.log('Download completed');
                    sendResponse({message: 'Download finished', sender: sender});
                    chrome.downloads.onChanged.removeListener(downloadListener);
                } else if (downloadDelta.state.current === "interrupted" && downloadDelta.error) {
                    console.log(`Download failed: ${downloadDelta.error}`);
                    sendResponse({message: 'Download failed'});
                    chrome.downloads.onChanged.removeListener(downloadListener);
                }
            }
        });
    });

    return true;
});
