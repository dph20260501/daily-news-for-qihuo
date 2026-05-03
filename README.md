# Daily Financial News System

## Project Overview
The Daily Financial News System collects and sends daily updates on financial news. The system is built using automated workflows to facilitate data fetching and email notifications.

## Prerequisites
- A Gmail account for sending emails.
- Access to GitHub to manage secrets for your repository.
- Familiarity with Git and GitHub Actions.

## Setting Up the Gmail App Password
1. Go to your [Google Account](https://myaccount.google.com/).
2. Navigate to "Security."
3. Under "Signing in to Google," find "App passwords."
4. If prompted, sign in to your Google Account.
5. Select the app you want to generate the password for (e.g., "Mail") and choose the device (e.g., "Other").
6. Click "Generate."
7. Copy the generated password as you will need it to configure the system.

## Configuring GitHub Actions Secrets
1. Navigate to your GitHub repository at `https://github.com/dph20260501/daily-news-for-qihuo`.
2. Click on "Settings."
3. In the sidebar, click on "Secrets and variables," then "Actions."
4. Click on "New repository secret."
5. Add the following secrets:
   - `GMAIL_USER`: Your Gmail address.
   - `GMAIL_APP_PASSWORD`: The app password you generated earlier.
6. Repeat for any other secrets required by your workflow.

## How the System Works
- The system employs GitHub Actions to automate the process of fetching financial news and sending it to subscribed users via email.
- On a scheduled basis, a workflow runs that retrieves the latest news articles.
- The articles are then compiled into a digest and sent to your configured email.

## License and Contact Information
For questions or contributions, please reach out or open an issue in the repository!