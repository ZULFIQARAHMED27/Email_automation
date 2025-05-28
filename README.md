# README
"""
# Email Marketing Automation

This script automates the process of sending personalized marketing emails to a list of clients. It reads client data from an Excel file, personalizes the email content for each recipient, and sends the emails using a Gmail account.

## Features
- Upload an Excel file containing client names and email addresses.
- Customize email templates with placeholders for personalization.
- Automatically send emails with a 15-second interval between each to avoid spam filters.

## Prerequisites
- Python 3.x installed on your system.
- Libraries:
  - pandas
  - openpyxl
- A Gmail account with 2-Step Verification enabled and an App Password generated.

## Setup Instructions
1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```bash
   pip install pandas openpyxl
   ```
3. Ensure your Gmail account has 2-Step Verification enabled and an App Password generated.

## Usage
1. Prepare an Excel file with the following columns:
   - `Name`: Client's name.
   - `Email`: Client's email address.

2. Run the script:
   ```bash
   python marketingmail.py
   ```

3. Enter the path to the Excel file, your Gmail address, and the generated App Password when prompted.

4. The script will send personalized emails to each client.

## Notes
- Ensure the Gmail account has "Allow less secure apps" enabled if not using App Passwords (not recommended).
- The script uses a 15-second interval between emails to comply with Gmail's sending limits.

## License
This project is open-source and available under the MIT License.
"""
