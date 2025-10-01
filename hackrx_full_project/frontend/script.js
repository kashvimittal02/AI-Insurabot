async function runHackRx() {
    const docUrl = document.getElementById('docUrl').value;
    const questions = document.getElementById('questions').value.split('\n').filter(q => q.trim() !== '');
    const res = await fetch('http://localhost:8000/hackrx/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer your_backend_auth_token_here'
        },
        body: JSON.stringify({ documents: docUrl, questions: questions })
    });
    const data = await res.json();
    document.getElementById('output').textContent = JSON.stringify(data, null, 2);
}
