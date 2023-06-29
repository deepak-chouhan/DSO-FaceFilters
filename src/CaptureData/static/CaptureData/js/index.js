function showOverlay() {
    const overlay = document.getElementById('overlay');
    const video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({video: true})
        .then((stream) => {
            video.srcObject = stream;
            console.log(stream)
            video.play();
            // video.onloadedmetadata = function(e) {
            //     overlay.style.display = 'flex';
            // };
        })
        .catch((error) => {
            console.error(error);
        });
}

// showOverlay();

function capture() {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const video = document.getElementById('video');
    const overlay = document.getElementById('overlay');
    const image = document.getElementById('image');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    video.pause();
    overlay.style.display = 'none';
    const imageDataURL = canvas.toDataURL('image/png');
    image.src = imageDataURL;
}