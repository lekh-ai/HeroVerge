function sendRequest() {
    const model = document.getElementById('model').value;
    const prompt = document.getElementById('prompt').value;
    const responseDiv = document.getElementById('response');

    fetch(`/${model}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `prompt=${encodeURIComponent(prompt)}`,
    })
        .then(response => response.json())
        .then(data => {
            // Clear previous response
            responseDiv.innerHTML = '';

            // Ensure the response is an object
            if (typeof data === 'string') {
                try {
                    data = JSON.parse(data);
                } catch (e) {
                    console.error('Error parsing JSON:', e);
                    responseDiv.textContent = 'Error: Invalid JSON response';
                    return;
                }
            }

            // Determine which parsing function to use based on the model
            let parsedData;
            if (model === 'llama2') {
                parsedData = parseProperties(data); // Using function 1
            } else {
                parsedData = parseKeyValuePairs(data); // Using function 2
            }

            // Display extracted key-value pairs in the HTML
            if (parsedData) {
                parsedData.forEach(({ key, value }) => {
                    const p = document.createElement('p');
                    p.innerHTML = `<span class="key">${key}:</span> ${value}`;
                    responseDiv.appendChild(p);
                });
            } else {
                responseDiv.textContent = 'Error: Unable to parse response.';
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            responseDiv.textContent = 'Error: ' + error;
        });
}

function parseProperties(data) {
    // Extract properties from 'properties' object
    const properties = data.properties;
    const requiredFields = data.required;

    // Extract and format key-value pairs
    const parsedData = requiredFields.map(key => ({
        key,
        value: properties[key].description
    }));

    return parsedData;
}

function parseKeyValuePairs(data) {
    // Extract key-value pairs directly from the object
    const parsedData = Object.entries(data).map(([key, value]) => ({
        key,
        value
    }));

    return parsedData;
}
