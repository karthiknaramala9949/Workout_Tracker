document.getElementById('addSetButton').addEventListener('click', function() {
    // Get the form element
    const form = document.getElementById('workoutForm');

    // Create a new div to hold the new workout set
    const newSet = document.createElement('div');
    newSet.classList.add('workout-set');

    // Add the input fields (date, type, duration) to the new set
    newSet.innerHTML = `
        <label for="date">Date:</label>
        <input type="date" name="date" required>
        <label for="type">Workout Type:</label>
        <select name="type" required>
            <option value="Running">Running</option>
            <option value="Push-Ups">Push-Ups</option>
            <option value="Yoga">Yoga</option>
            <option value="Weight-Lifting">Weight-Lifting</option>
        </select>
        <label for="duration">Duration (minutes):</label>
        <input type="number" name="duration" required>
    `;

    // Append the new set to the form
    form.insertBefore(newSet, document.getElementById('addSetButton'));
});
