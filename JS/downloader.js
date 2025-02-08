const fs = require('fs'); // File system module for writing the downloaded file
const ytdl = require('ytdl-core'); // YouTube downloader module

// Retrieve command line arguments: video URL and optional name
const videoUrl = process.argv[2];
var name = process.argv[3];

// Function to update the file name if not provided
function updateNameIfNeeded(newName) {
  if (!name || name == "") {
    name = newName;
  }
}

// Asynchronous function to download audio from the given YouTube URL
async function downloadAudio() {
  if (!ytdl.validateURL(videoUrl)) { // Validate if the provided URL is a YouTube link
    console.log('Invalid YouTube URL');
    return;
  }

  // Fetch video details
  const info = await ytdl.getInfo(videoUrl);
  updateNameIfNeeded(info.videoDetails.title); // Update file name if necessary
  console.log(info.videoDetails.title); // Log video title
  console.log(info.videoDetails.videoId); // Log video ID

  // Filter to extract only audio (webm format)
  const audioFilter = (format) => format.container === 'webm' && !format.hasVideo;
  const stream = ytdl(videoUrl, { filter: audioFilter });

  // Pipe the stream to a file and handle completion or errors
  stream.pipe(fs.createWriteStream(`${name}.webm`))
    .on('finish', () => console.log('Download complete!'))
    .on('error', (err) => console.error('Download error:', err));
}

// Start the audio download process
downloadAudio();
