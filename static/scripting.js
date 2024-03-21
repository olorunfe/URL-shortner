async function handleTrimUrl(event) {
    event.preventDefault();

    const longUrl = document.getElementById('long-url-input').value;
    const customAlias = document.getElementById('custom-alias-input').value;

    const response = await fetch('/shorten-url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ long_url: longUrl, custom_alias: customAlias })
    });

    if (response.ok) {
      const data = await response.json();
      const shortenedUrl = data.shortened_url;
      document.getElementById('shortened-url-input').value = shortenedUrl;
      document.getElementById('shortened-url-container').style.display = 'block';
    } else {
      console.error('Failed to shorten URL');
    }
  }

  // Function to copy the shortened URL to clipboard
  function copyUrlToClipboard() {
    const urlInput = document.getElementById('shortened-url-input');
    urlInput.select();
    document.execCommand('copy');
    alert('URL copied to clipboard');
  }

  // Add event listener to the copy URL button
  const copyButton = document.getElementById('copy-url-button');
  copyButton.addEventListener('click', copyUrlToClipboard);