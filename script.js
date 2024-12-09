document.addEventListener('DOMContentLoaded', function() {
    // Initialize Flatpickr with custom styling
    flatpickr("#birthdate", {
        dateFormat: "F j, Y",
        maxDate: "today",
        minDate: "1900-01-01",
        defaultDate: "today",
        animate: true,
        theme: "material_blue",
        disableMobile: false,
        monthSelectorType: "dropdown",
        position: "auto",
        showMonths: 1,
        static: true,
        yearSelectorType: "dropdown",
        onChange: function(selectedDates, dateStr) {
            // Add subtle animation when date changes
            const input = document.getElementById('birthdate');
            input.style.transform = 'scale(1.02)';
            setTimeout(() => {
                input.style.transform = 'scale(1)';
            }, 200);
        },
        onOpen: function(selectedDates, dateStr, instance) {
            // Add animation when calendar opens
            instance.calendarContainer.style.transform = 'translateY(10px)';
            instance.calendarContainer.style.opacity = '0';
            setTimeout(() => {
                instance.calendarContainer.style.transform = 'translateY(0)';
                instance.calendarContainer.style.opacity = '1';
            }, 0);
        }
    });

    const calculateBtn = document.getElementById('calculateBtn');
    const resultText = document.getElementById('result');
    const birthdateInput = document.getElementById('birthdate');

    calculateBtn.addEventListener('click', calculateAgeWithAnimation);
    birthdateInput.addEventListener('change', calculateAgeWithAnimation);

    function calculateAgeWithAnimation() {
        // Add loading state
        calculateBtn.classList.add('loading');
        resultText.textContent = "Calculating...";

        // Simulate loading for smooth animation
        setTimeout(() => {
            calculateAge();
            calculateBtn.classList.remove('loading');
        }, 500);
    }

    function calculateAge() {
        try {
            const birthDate = new Date(birthdateInput.value);
            const today = new Date();

            if (birthDate > today) {
                showResult("🤔 You haven't been born yet!");
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

            const result = `✨ Your magical age is:\n${years} years, ${months} months, and ${days} days! 🎉\n\nBorn on: ${birthDate.toLocaleDateString('en-US', { 
                month: 'long', 
                day: 'numeric', 
                year: 'numeric' 
            })}`;
            
            showResult(result);

        } catch (error) {
            showResult("An error occurred. Please try again.");
        }
    }

    function showResult(text) {
        resultText.style.opacity = '0';
        
        setTimeout(() => {
            resultText.textContent = text;
            resultText.style.opacity = '1';
            resultText.classList.remove('bounce');
            void resultText.offsetWidth; // Trigger reflow
            resultText.classList.add('bounce');
        }, 200);
    }
}); 