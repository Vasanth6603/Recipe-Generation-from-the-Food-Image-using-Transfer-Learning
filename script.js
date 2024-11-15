function uploadImage() {
    const input = document.getElementById('imageUpload');
    const file = input.files[0];
    const formData = new FormData();
    formData.append('file', file);
  
    fetch('/upload', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('results').innerHTML = `
        <h2>Predicted Food Item: ${data.food_item}</h2>
        <h3>Recipe:</h3>
        <p>${data.recipe}</p>
      `;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  