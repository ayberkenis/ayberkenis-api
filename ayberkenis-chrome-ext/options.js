document.addEventListener('DOMContentLoaded', function () {
    const selectElement = document.getElementById('api-path-select');
    const statusElement = document.getElementById('api-status');
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