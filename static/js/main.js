function updateStats() {
    fetch('/stats')
        .then(response => response.json())
        .then(data => {
            // Update CPU stats
            document.getElementById('cpu-percent').textContent = data.cpu_percent.toFixed(1);
            document.getElementById('cpu-temp').textContent = data.cpu_temp.toFixed(1);
            
            // Update Memory stats
            document.getElementById('memory-used').textContent = data.memory.used;
            document.getElementById('memory-total').textContent = data.memory.total;
            document.getElementById('memory-bar').style.width = `${data.memory.percent}%`;
            
            // Update Disk stats
            document.getElementById('disk-used').textContent = data.disk.used;
            document.getElementById('disk-total').textContent = data.disk.total;
            document.getElementById('disk-bar').style.width = `${data.disk.percent}%`;
        })
        .catch(error => console.error('Error fetching stats:', error));
}

// Update stats every 2 seconds
setInterval(updateStats, 2000);
// Initial update
updateStats();
