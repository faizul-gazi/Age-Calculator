document.addEventListener('DOMContentLoaded', function() {
    const dayInput = document.getElementById('day');
    const monthInput = document.getElementById('month');
    const yearInput = document.getElementById('year');
    const calculateBtn = document.getElementById('calculateBtn');
    const resultText = document.getElementById('result');

    // Populate year dropdown
    const currentYear = new Date().getFullYear();
    for (let year = currentYear; year >= 1900; year--) {
        const option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        yearInput.appendChild(option);
    }

    // Add input validation
    dayInput.addEventListener('input', validateDay);
    monthInput.addEventListener('change', validateDay);
    yearInput.addEventListener('change', validateDay);

    function validateDay() {
        const day = parseInt(dayInput.value);
        const month = parseInt(monthInput.value);
        const year = parseInt(yearInput.value);
        
        if (!isNaN(month) && !isNaN(year)) {
            const lastDay = new Date(year, month + 1, 0).getDate();
            dayInput.max = lastDay;
            
            if (day > lastDay) {
                dayInput.value = lastDay;
            } else if (day < 1) {
                dayInput.value = 1;
            }
        }
    }

    calculateBtn.addEventListener('click', calculateAgeWithAnimation);

    function calculateAgeWithAnimation() {
        if (!validateInputs()) {
            return;
        }

        calculateBtn.classList.add('loading');
        resultText.textContent = "Calculating...";

        setTimeout(() => {
            calculateAge();
            calculateBtn.classList.remove('loading');
        }, 500);
    }

    function validateInputs() {
        let isValid = true;
        const inputs = [dayInput, monthInput, yearInput];
        
        inputs.forEach(input => {
            if (!input.value) {
                input.classList.add('input-error');
                isValid = false;
                setTimeout(() => input.classList.remove('input-error'), 500);
            }
        });

        if (!isValid) {
            showResult("Please fill in all date fields!");
            return false;
        }

        // Additional validation for valid date
        const day = parseInt(dayInput.value);
        const month = parseInt(monthInput.value);
        const year = parseInt(yearInput.value);
        
        const date = new Date(year, month, day);
        if (date.getFullYear() !== year || date.getMonth() !== month || date.getDate() !== day) {
            showResult("Please enter a valid date!");
            return false;
        }

        return true;
    }

    function calculateAge() {
        try {
            const birthDate = new Date(
                parseInt(yearInput.value),
                parseInt(monthInput.value),
                parseInt(dayInput.value)
            );
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
            showResult("Please enter a valid date!");
        }
    }

    function showResult(text) {
        resultText.style.opacity = '0';
        
        setTimeout(() => {
            resultText.textContent = text;
            resultText.style.opacity = '1';
            resultText.classList.remove('bounce');
            void resultText.offsetWidth;
            resultText.classList.add('bounce');
        }, 200);
    }
}); 