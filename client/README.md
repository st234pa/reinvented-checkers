# Reinvented Checkers Client App (React Native)

## Setup (for Mac)

### Node

- Make sure you have [node and npm](https://nodejs.org/en/download/) installed. If you don't have it installed, use the macOS installer.
- Make sure you have [yarn](https://classic.yarnpkg.com/en/docs/install#mac-stable) installed.

### Expo

- Install the Expo CLI command line utility.
```
npm install -g expo-cli
```
- On your phone, install the Expo Client app from App Store or Google Play.

## Running the app locally

- Clone this repository. 
- Run the API locally following the instructions from `api/README.md`.
- From the `reinvented-checkers/client/app` directory, install dependancies for the app.
```
:app $ yarn
```
- In the `reinvented-checkers/client/app` directory, run a local Metro server for the app.
```
:app $ yarn start
```
- Make sure your phone is connected to the same network as the Metro server.
- Run the app on your phone in Expo Client. For an iPhone, use the Camera app to scan the QR code, which should result in a notification that opens the app in Expo when you open it. For an Android, press "Scan QR Code" on the "Projects" tab of the Expo client app and scan the QR code you see in the terminal or in Expo Dev Tools.
