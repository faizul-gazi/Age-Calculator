document.addEventListener('DOMContentLoaded', function() {
    const dayInput = document.getElementById('day');
    const monthInput = document.getElementById('month');
    const yearInput = document.getElementById('year');
    const calculateBtn = document.getElementById('calculateBtn');
    const resultText = document.getElementById('result');

    // Set max year to current year
    yearInput.max = new Date().getFullYear();

    // Add input validation
    dayInput.addEventListener('input', validateDay);
    monthInput.addEventListener('change', validateDay);
    yearInput.addEventListener('input', validateYear);

    function validateDay() {
        const day = parseInt(dayInput.value);
        const month = parseInt(monthInput.value);
        const year = parseInt(yearInput.value);
        
        if (month !== null && year) {
            const lastDay = new Date(year, month + 1, 0).getDate();
            dayInput.max = lastDay;
            
            if (day > lastDay) {
                dayInput.value = lastDay;
            }
        }

        if (day < 1) {
            dayInput.value = 1;
        }
    }

    function validateYear() {
        const year = parseInt(yearInput.value);
        const currentYear = new Date().getFullYear();
        
        if (year > currentYear) {
            yearInput.value = currentYear;
        }
        if (year < 1900) {
            yearInput.value = 1900;
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

        return true;
    }

    function calculateAge() {
        try {
            const birthDate = new Date(
                yearInput.value,
                monthInput.value,
                dayInput.value
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