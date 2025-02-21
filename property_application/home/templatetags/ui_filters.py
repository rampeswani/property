from django import template

register = template.Library()

def convert_to_lakh_crore(value):
    try:
        value = int(value)  # Ensure value is an integer
    except ValueError:
        return value  # Return as is if not a number

    if value >= 10**7:  # 1 Crore and above
        return f"{value / 10**7:.1f} Cr"
    elif value >= 10**5:  # 1 Lakh and above
        return f"{value / 10**5:.1f} L"
    else:  # Below 1 Lakh, return as is
        return f"{value:,}"  # Formats with commas (e.g., 75,000)

register.filter("to_lakh_crore", convert_to_lakh_crore)
