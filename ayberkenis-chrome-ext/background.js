chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
    console.log('message received')
    console.log(message);
    chrome.storage.sync.get('apiPath', function (data) {
        let baseUrl = '';
        if (data.apiPath === 'local') {
            baseUrl = 'http://127.0.0.1:5000/api/v1';
        } else if (data.apiPath === 'production') {
            baseUrl = 'https://ayberkenis.com.tr/api/v1';
        }


        let url = baseUrl + '/downloader/' + message.source + '/' + message.id;
        console.log(url);
        const downloadOptions = {
            url: url,
            method: 'GET',
            saveAs: true,
            headers: [
                {name: 'Content-Type', value: 'application/json'}
            ]
        };

        chrome.downloads.download(downloadOptions, function (downloadId) {
            chrome.downloads.onChanged.addListener(function downloadListener(downloadDelta) {
                console.log(downloadDelta);
                if (downloadDelta.id === downloadId && downloadDelta.state) {
                    if (downloadDelta.state.current === "complete") {

                        sendResponse({message: 'finished', sender: sender});
                        chrome.downloads.onChanged.removeListener(downloadListener);
                    } else if (downloadDelta.error && downloadDelta.error.current === 'USER_CANCELED') {
                        sendResponse({message: 'cancelled', sender: sender});
                        chrome.downloads.onChanged.removeListener(downloadListener);
                    }
                    else if (downloadDelta.state.current === "interrupted") {
                        sendResponse({message: 'failed', sender: sender});
                        chrome.downloads.onChanged.removeListener(downloadListener);
                    }
                }
            });
        });

    });
    return true;
});
