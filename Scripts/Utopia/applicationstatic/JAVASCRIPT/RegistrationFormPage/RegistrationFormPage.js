// Get the drop-area and img-view elements
const dropArea = document.getElementById('drop-area');
const imgView = document.getElementById('img-view');
console.log("hit bro")
const inputFile = document.getElementById('input-file');

// Handle file selection
inputFile.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        displayImage(file);
        console.log("there is a file ")
    }
});

// Handle dragover event
dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dropArea.classList.add('dragging'); // Optional: add a visual indicator for dragging
});

// Handle dragleave event
dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('dragging');
});

// Handle drop event
dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    dropArea.classList.remove('dragging');
    const file = event.dataTransfer.files[0];
    if (file) {
        displayImage(file);
    }
});

// Function to display the selected image
function displayImage(file) {
    const reader = new FileReader();
    reader.onload = function (e) {
        const img = document.createElement('img');
        img.src = e.target.result; // Set the image source to the file content
        img.alt = 'Uploaded Image';
        imgView.innerHTML = ''; // Clear the current contents
        imgView.appendChild(img); // Add the new image to the view
    };
    reader.readAsDataURL(file); // Read the file as a data URL
}
