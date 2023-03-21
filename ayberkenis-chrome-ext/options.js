const downloadDirectoryInput = document.getElementById('download-directory');
const saveButton = document.getElementById('save-button');

chrome.storage.sync.get('downloadDirectory', (data) => {
  if (data.downloadDirectory) {
    downloadDirectoryInput.value = data.downloadDirectory;
  }
});

saveButton.addEventListener('click', () => {
  const downloadDirectory = downloadDirectoryInput.value;
  chrome.storage.sync.set({ downloadDirectory }, () => {
    alert('Settings saved');
  });
});
