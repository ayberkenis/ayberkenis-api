document.addEventListener('DOMContentLoaded', function () {
    const selectElement = document.getElementById('api-path-select');
    const statusElement = document.getElementById('api-status');
    const resolutionESelect = document.getElementById('resolution-select');
    const videoFormatSelect = document.getElementById('video-format-select');
    const audioFormatSelect = document.getElementById('audio-format-select');
    console.log(selectElement);
    chrome.storage.sync.get('apiPath', function (data) {
        // Set the default selected option based on the saved value
        console.log(selectElement.value)
        console.log(data)
        if (data.apiPath === 'local') {
            selectElement.value = 'local';
        } else if (data.apiPath === 'production') {
            selectElement.value = 'production';
        }
    });
    chrome.storage.sync.get('resolution', function (data) {
        // Set the default selected option based on the saved value
        console.log(resolutionESelect.value)
        console.log(data)
        if (data.resolution === 'best') {
            resolutionESelect.value = 'best';
        } else if (data.resolution === '2160p') {
            resolutionESelect.value = '2160p';
        } else if (data.resolution === '1080p') {
            resolutionESelect.value = '1080p';
        } else if (data.resolution === '720p') {
            resolutionESelect.value = '720p';
        } else if (data.resolution === '480p') {
            resolutionESelect.value = '480p';
        } else if (data.resolution === '360p') {
            resolutionESelect.value = '360p';
        }
    });
    fetch('https://ayberkenis.com.tr/api/v1/status')
        .then(response => response.json())
        .then(data => {
            if (data.message === 'OK') {
                statusElement.innerHTML = '<span class="badge bg-success">Online</span>';
            } else {
                statusElement.innerHTML = '<span class="badge bg-danger">Offline</span>';
            }
        });
});