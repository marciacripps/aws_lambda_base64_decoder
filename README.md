# AWS Lambda Base64 Decoder

This project is a simple Base64 Decoder web app built using **Vite (Vue.js)** for the frontend, and **AWS Lambda** and **API Gateway** for the backend. The app allows users to input a Base64 encoded string, decode it using an AWS Lambda function, and display the decoded output on the frontend. The project is deployed on **Netlify**.

## Project Overview

- **Frontend**: Vite (Vue.js), Tailwind CSS
- **Backend**: AWS Lambda (Python), API Gateway
- **Hosting**: Netlify for frontend, AWS Lambda and API Gateway for backend
- **Build Tool**: Vite
- **Environment Variables**: Managed via Netlify for frontend

## Features

- Base64 input field where users can submit an encoded string.
- Upon submission, the string is sent to the backend (AWS Lambda) via an API request.
- The backend decodes the Base64 string and returns the decoded value.
- The decoded value is displayed on the frontend.

## Technologies Used

### Frontend
- **Vue.js**: A progressive JavaScript framework for building user interfaces.
- **Vite**: A fast build tool and development server for Vue.js.
- **Tailwind CSS**: (Optional) Utility-first CSS framework used for styling.
- **Netlify**: Platform for deploying and hosting the frontend.

### Backend
- **AWS Lambda**: A serverless computing service that runs the Base64 decoding logic.
- **API Gateway**: Used to expose the Lambda function as an HTTP endpoint.
- **DynamoDB**: (Future Integration) Intended to record user submissions.

## How It Works

1. The user enters a Base64 encoded string into the input field on the web app.
2. The app makes a `POST` request to an AWS API Gateway endpoint, sending the encoded string.
3. The API Gateway triggers an AWS Lambda function that decodes the Base64 string.
4. The Lambda function returns the decoded result, which is displayed on the frontend.
