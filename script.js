document.addEventListener('DOMContentLoaded', function() {
    // Initialize Flatpickr
    flatpickr("#birthdate", {
        dateFormat: "Y-m-d",
        maxDate: "today",
        minDate: "1900-01-01",
        defaultDate: "today"
    });

    const calculateBtn = document.getElementById('calculateBtn');
    const resultText = document.getElementById('result');
    const birthdateInput = document.getElementById('birthdate');

    calculateBtn.addEventListener('click', calculateAge);
    birthdateInput.addEventListener('change', calculateAge);

    function calculateAge() {
        try {
            const birthDate = new Date(birthdateInput.value);
            const today = new Date();

            if (birthDate > today) {
                resultText.textContent = "🤔 You haven't been born yet!";
                return;
            }

            let years = today.getFullYear() - birthDate.getFullYear();
            let months = today.getMonth() - birthDate.getMonth();
            let days = today.getDate() - birthDate.getDate();

            if (days < 0) {
                months--;
                const lastMonth = new Date(today.getFullYear(), today.getMonth(), 0);
                days += lastMonth.getDate();
            }

            if (months < 0) {
                years--;
                months += 12;
            }

            const result = `✨ Your magical age is:\n${years} years, ${months} months, and ${days} days! 🎉\nBorn on: ${birthDate.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}`;
            
            resultText.textContent = result;
            
            // Add bounce animation
            resultText.classList.remove('bounce');
            void resultText.offsetWidth; // Trigger reflow
            resultText.classList.add('bounce');

        } catch (error) {
            resultText.textContent = "An error occurred. Please try again.";
        }
    }
}); 